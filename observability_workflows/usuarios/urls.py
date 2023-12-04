from django.urls import path, include
from observability_workflows.views import index
from usuarios import views_login
from usuarios import views_logout
from usuarios import views_perfil
from usuarios import views_registro

urlpatterns = [
    path('', view=index, name='index'),
    path('login', view=views_login.login, name='login'),
    path('logout', view=views_logout.logout, name='logout'),
    path('register', view=views_registro.register, name='register'),
]