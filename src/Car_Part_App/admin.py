from django.contrib import admin

# Register your models here.
from .models import Car,Category

# car model register
admin.site.register(Car)
admin.site.register(Category)