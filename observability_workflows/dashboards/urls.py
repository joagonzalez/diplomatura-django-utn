from dashboards import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='dashboards'),
]