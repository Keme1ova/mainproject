from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home' ),
	path('premium/', views.catalog1, name = 'premium' ),
	path('jeep/', views.catalog2, name = 'jeep' ),
	path('limousine/', views.catalog3, name = 'limousine' ),
	path('cabriolet/', views.catalog4, name = 'cabriolet' ),
	path('retro/', views.catalog5, name = 'retro' ),
	path('transfer/', views.catalog6, name = 'transfer' ),
]
