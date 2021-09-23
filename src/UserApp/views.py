from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
<<<<<<< HEAD
from django.urls import reverse
from .forms import SellerSignUpFrom, BuyerSignupForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse


# Create your views here.
# Signup View
class SignupView(TemplateView, LoginRequiredMixin):
    template_name = 'registration/signup_form.html'


# Userview
class BuyerSignUpView(CreateView, UserPassesTestMixin):
=======
from django.urls import  reverse
from .forms import SellerSignUpFrom, BuyerSignupForm
from .models import User
from  django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from django.http import  HttpResponse

# Create your views here.
# Signup View
class SignupView(TemplateView,LoginRequiredMixin):
    template_name = 'registration/signup_form.html'

# Userview
class BuyerSignUpView(CreateView,UserPassesTestMixin):
>>>>>>> 63fc51b4f4b5d3d416a2c60a364cc7713909ce53
    model = User
    form_class = BuyerSignupForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_role'] = 'Buyer'
        return super().get_context_data(**kwargs)

<<<<<<< HEAD
    def test_func(self):
        role = self.get_object()
        if self.request.user == role.Buyer:
            return True
        return False

=======
    # def get(self, request, *args, **kwargs):
    #     role = self.request.user.user_role
    #     print(role)
    #     if role == 0:
    #         return redirect(reverse('Car_Part_App:CarCreateView'))
>>>>>>> 63fc51b4f4b5d3d416a2c60a364cc7713909ce53

class LoginTempView(View):

    def get(self, request, *args, **kwargs):
        if request.user.user_role == 0:
<<<<<<< HEAD
            return redirect(reverse('Car_Part_App:Data'))
        else:
            return redirect(reverse('Car_Part_App:Data'))


# seller Signup
class SellerSignUpView(CreateView, UserPassesTestMixin):
=======
            return redirect(reverse('Car_Part_App:parts_data'))
        else:
            return redirect(reverse('Car_Part_App:Data'))

# seller Signup
class SellerSignUpView(CreateView):
>>>>>>> 63fc51b4f4b5d3d416a2c60a364cc7713909ce53
    model = User
    form_class = SellerSignUpFrom
    template_name = "registration/signup.html"

    # to get user type
    def get_context_data(self, **kwargs):
<<<<<<< HEAD
        kwargs['user_role'] = 'Seller'
=======
        kwargs['user_role'] = 'seller'
>>>>>>> 63fc51b4f4b5d3d416a2c60a364cc7713909ce53
        return super().get_context_data(**kwargs)

    # def form_valid(self, form):
    #      user = form.save()
    #      return redirect('Car_Part_App:CarCreateView')
<<<<<<< HEAD
    def test_func(self):
        role = self.get_object()
        if self.request.user == role.Seller:
            return True
        return False
=======


>>>>>>> 63fc51b4f4b5d3d416a2c60a364cc7713909ce53
