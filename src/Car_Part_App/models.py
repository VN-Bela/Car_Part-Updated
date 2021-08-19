from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.

user = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


Part_Info = (
    ('New', "New"),
    ('Use', "Use"),
)


# Car Part Model
class Car(models.Model):
    Car_name = models.CharField(max_length=100, null=True)
    Car_model = models.CharField(max_length=100, null=True)
    Car_Part_Name = models.CharField(max_length=100, null=True)
    Car_Part_Info = models.CharField(max_length=50, choices=Part_Info)
    Car_Part_Discription = models.CharField(max_length=100, null=True)
    Owner_info = models.CharField(max_length=200, null=True)
    seller = models.ForeignKey(user, related_name="Car_Part_App", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Car_Part_Name
