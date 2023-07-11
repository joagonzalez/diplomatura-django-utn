from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    params = {}
    params['site_name'] = 'Observability Insights Index page'
    params['page'] = 'index.html'
    
    return render(request, 'observability_workflows/index.html', params)
