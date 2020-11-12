from django.urls import path
from . import views

urlpatterns = [
    
    path('Inicio', views.Inicio, name = 'Inicio'),
    path('Galeria', views.Galeria, name = 'Galeria'),
    path('registro', views.registro, name='registro'),
    path('RegistroProductos', views.RegistroProductos, name='RegistroProductos')
                ]
