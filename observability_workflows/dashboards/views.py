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
