from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('', view=views.index, name='index'),
]