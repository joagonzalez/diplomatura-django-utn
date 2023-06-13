from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Observability Insights'
    params['page'] = 'dashboards.html'
    
    return render(request, 'dashboards/index.html', params)
