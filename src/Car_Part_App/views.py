from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.core.mail import send_mail
from .models import Car, Category
from .forms import Car_Part_Form
from django.urls import reverse
from django.conf import settings
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from django.views.generic.base import TemplateView
from django.core.mail import send_mail
# from .filters import CategoryFilter
from .models import Car, Category
from django.contrib.auth import login
from .forms import Car_Part_Form
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage

# from django_filters.views import  FilterView



# Create your views here.
# function based View
# def index(request):
# return HttpResponse("Welcome to Car Part Selling ")
#  return render(request,'Car/index.html')

# class based View
class CarListView(ListView):
    model = Car
    context_object_name = 'parts'
    paginate_by = 2
    queryset = Car.objects.all()
    template_name = 'Car/index.html'

    def get(self, request):
        category_name = request.GET.get('category_name', None)
        if category_name == None:
            parts = Car.objects.all()
        else:
            parts = Car.objects.filter(category=category_name)
        categories = Category.objects.all()
        context = {
            "parts": parts,
            "categories": categories
        }
        return render(request, self.template_name, context)


#
# class CategoryList(FilterView):
#     model=Category
#     filter_class=CategoryFilter
#     template_name = "Car/index.html"

class CarCreateView(CreateView):
    model = Car
    template_name = 'Car/CarHome.html'
    form_class = Car_Part_Form

    # fields = [
    #     'Car_name',
    #     'Car_model',
    #     'Car_Part_Name',
    #     'Car_Part_Info',
    #     'Car_Part_Cat',
    #     'Car_Part_Discription',
    #     'Owner_info',
    # ]
    def post(self, request, *args, **kwargs):
        form = Car_Part_Form(request.POST or None, request.FILES)
        if form.is_valid():
            car_part = form.save(commit=False)
            car_part.seller = request.user
            # car_part.Part_Image = request.FILES['Part_Image']
            car_part.save()

        return redirect(reverse('Car_Part_App:parts_data'))

    def get(self, request, *args, **kwargs):
        # return redirect(reverse('Car_Part_App:parts_data'))
        if request.user.user_role == 0:
            form = Car_Part_Form()
            context = {
                'form':form
            }
            return render(request, self.template_name, context=context)
        else:
            return redirect(reverse('UserApp:logout'))


    # def test_func(self):
    #     role = self.get_object()
    #     if self.request.user == role.seller:
    #         return True
    #     return False
        return redirect(reverse('Car_Part_App:Data'))



class CarDetailView(DetailView):
    model = Car
    template_name = "Car/Car_detail.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Car, pk=pk)


class shopDetailsView(DetailView):
    model = Car
    template_name = "Buyer/shop.html"
    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(Car,pk=pk)


# class OrderConfrimView(ListView):
#     model= Car
#     template_name="Buyer/orderconfirm.html"

def sendmail(request,pk):
    post=Car.objects.get(pk=pk)
    user=request.user
    subject ="Order Received"
    messege= f"Your {post.Car_Part_Name} Part has been Purchased By {user.username}"
    sender=settings.EMAIL_HOST_USER
    reciver={'bela.vnurture@gmail.com'}
    send_mail(
        subject,messege,sender,reciver
    )
    return render(request,"Buyer/orderconfirm.html")

