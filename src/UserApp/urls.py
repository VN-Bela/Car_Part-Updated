from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views

app_name = "UserApp"

urlpatterns = [

    path('',include('django.contrib.auth.urls')),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("signup/buyer", views.BuyerSignUpView.as_view(), name="buyer_signup"),
    path("signup/seller", views.SellerSignUpView.as_view(), name="seller_signup"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("login_temp", views.LoginTempView.as_view(), name='login_temp')

]