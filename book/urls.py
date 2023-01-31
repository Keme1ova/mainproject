from django.urls import path
from . import views

urlpatterns = [
   path('order/', views.OrderCreate.as_view(), name='added'),
]