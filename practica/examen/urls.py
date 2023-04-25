from django.urls import path

from . import views

app_name='examen'

urlpatterns = [
    path('', views.index,name='index'),
    path('resolver', views.resolver, name='resolver'),
    path('registro', views.registro, name='registro')
]
