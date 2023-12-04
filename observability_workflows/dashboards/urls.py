from dashboards import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main'),
    path('ecobici/', views.ecobici, name='ecobici'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    # path('usecases/', views.usecases, name='usecases'),
]