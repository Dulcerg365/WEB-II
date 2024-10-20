from django.urls import path
from . import views

urlpatterns = [
    path('', views.estados_municipios, name='estados_municipios'),
    path('municipios/', views.municipios, name='municipios'),
]
