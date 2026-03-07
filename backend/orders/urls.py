from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order),
    path('vieworders/', views.get_orders),
]