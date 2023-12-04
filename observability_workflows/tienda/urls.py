from tienda import views
# from tienda.views import index #, verImagenes
from django.urls import path

urlpatterns = [
    path('', views.index, name='tienda'),
    path('cargar/', views.cargar_imagen, name='cargar'),
    # path('ver/', VerImagenes.as_view(), name='verImagenes'),
    # path('ver/<int:dashboard_id>/', views.ver_imagen, name='verImagene'),
]