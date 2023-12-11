"""observability_workflows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from observability_workflows import views
from django.conf.urls.static import static
from django.urls import path, include, re_path
from tienda.sitemap import TiendaSiteMap
from dashboards.sitemap import DashboardsSiteMap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

sitemaps = {
    'dashboards': DashboardsSiteMap,
    'tienda': TiendaSiteMap,
}

urlpatterns = [
    # path('', view=views.index, name='index'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('', include('dashboards.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('captcha/', include('captcha.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('accounts/', include('registration.backends.default.urls'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]