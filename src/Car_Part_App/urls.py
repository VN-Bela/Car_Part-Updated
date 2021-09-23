from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Car_Part_App'

urlpatterns = [
    path('', views.CarListView.as_view(), name="Data"),
    # path('', views.index ,name="Data"),
    path('parts_data/', views.CarCreateView.as_view(), name='parts_data'),
    path("car_detail/<int:pk>", views.CarDetailView.as_view(), name="car_detail"),
    path("shop/<int:pk>", views.shopDetailsView.as_view(), name="shop"),
    path("Orderconfirm/<int:pk>", views.sendmail, name="Orderconfirm"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
