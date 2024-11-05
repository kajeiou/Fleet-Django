from django.urls import path
from .views import vehicle_list, vehicle_detail, add_vehicle

urlpatterns = [
    path('vehicles/add/', add_vehicle, name='add_vehicle'),
    path('', vehicle_list, name='vehicle_list'),
    path('<int:pk>/', vehicle_detail, name='vehicle_detail'),
]
