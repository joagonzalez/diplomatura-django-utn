from dashboards import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='dashboards'),
    path('responsive/', views.responsive, name='responsive'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('carrusel/', views.carrusel, name='carrusel'),
]