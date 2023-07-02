from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Observability Insights'
    params['page'] = 'dashboards.html'
    
    return render(request, 'dashboards/index.html', params)

def responsive(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Responsive stylesheets'
    params['page'] = 'responsive.html'
    
    return render(request, 'dashboards/responsive.html', params)

def bootstrap(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Responsive stylesheets using bootstrap'
    params['page'] = 'bootstrap_styles.html'
    
    return render(request, 'dashboards/bootstrap_styles.html', params)

def carrusel(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Responsive stylesheets using bootstrap'
    params['page'] = 'carrusel.html'
    
    return render(request, 'dashboards/carrusel.html', params)

def modal(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Responsive stylesheets using bootstrap'
    params['page'] = 'modal.html'
    
    return render(request, 'dashboards/modal.html', params)