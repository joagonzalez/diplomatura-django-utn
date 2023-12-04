from django.shortcuts import render
from dashboards.models import Dashboards
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login')
def index(request):
    params = {}
    params['page_name'] = 'Observability Insights'
    params['page'] = 'index.html'
    params['data'] = Dashboards.objects.all()
    
    return render(request, 'dashboards/index.html', params)

@login_required(login_url='/accounts/login')
def ecobici(request):
    params = {}
    params['site_name'] = 'Observability Insights - Ecobici'
    params['page'] = 'ecobici.html'
    
    return render(request, 'dashboards/ecobici.html', params)

@login_required(login_url='/accounts/login')
def infrastructure(request):
    params = {}
    params['site_name'] = 'Observability Insights - Infrastructure'
    params['page'] = 'infrastructure.html'
    
    return render(request, 'dashboards/infrastructure.html', params)

@login_required(login_url='/accounts/login')
def usecases(request):
    params = {}
    params['site_name'] = 'Observability Insights - Usecases'
    params['page'] = 'usecases.html'
    
    return render(request, 'dashboards/usecases.html', params)

