from django.urls import path
from . import views
urlpatterns = [
    path('addcart/',views.AddCart.as_view()),
    path('viewcart/', views.ViewCart.as_view()),
]