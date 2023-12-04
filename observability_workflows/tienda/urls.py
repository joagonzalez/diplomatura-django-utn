from tienda import views
from tienda.views import index, Usecases
from django.urls import path

urlpatterns = [
    path('', Usecases.as_view(), name='usecases'),
    path('cargar/', views.cargar_dashboard, name='cargar'),
    path('usecases/', Usecases.as_view(), name='usecases'),
    path('usecase/<int:dashboard_id>/', views.usecase, name='usecase'),
]