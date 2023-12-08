from tienda import views
from tienda.views import index, Usecases, SearchDashboard
from django.urls import path

urlpatterns = [
    path('', Usecases.as_view(), name='usecases'),
    path('cargar/', views.cargar_dashboard, name='cargar'),
    path('usecases/', Usecases.as_view(), name='usecases'),
    path('usecase/<int:dashboard_id>/', views.usecase, name='usecase'),
    path('scroll/', views.scroll, name='scroll'),
    path('scroll_raw/', views.scroll_raw, name='scroll_raw'),
    path('landing/', views.landing, name='landing'),
    path('landing_raw/', views.landing_raw, name='landing_raw'),
    path('search/', views.search, name='search'),
    path('search_dashboard/', SearchDashboard.as_view(), name='search_dashboard'),
]