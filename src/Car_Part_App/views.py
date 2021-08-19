from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import TemplateView

#from .filters import CategoryFilter
from .models import Car, Category
from django.contrib.auth import login
from .forms import Car_Part_Form
from django.urls import reverse
from django.conf import settings
#from django_filters.views import  FilterView


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
        if category_name ==  None:
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
        form = Car_Part_Form(request.POST or None)
        if form.is_valid():
            car_part = form.save(commit=False)
            car_part.seller = request.user
            car_part.save()
        return redirect(reverse('Car_Part_App:Data'))


class CarDetailView(DetailView):
    model = Car
    template_name = "Car/Car_detail.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Car, pk=pk)
