import json
from django.http import HttpResponse
from requests import Request
from django.http import Http404
from django.views.generic import View 
from django.shortcuts import render, redirect
from tienda.forms import CargarForm, SearchDashboardForm
from dashboards.models import Dashboards
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='/' , login_url='/usuarios/login')
def index(request: Request):
    params = {}
    params['site_name'] = 'Observability Insights - Tienda'
    params['page'] = 'tienda.html'
    
    return render(request, 'tienda/index.html', params)

@login_required(redirect_field_name='/' , login_url='/usuarios/login')
def cargar_dashboard(request: Request):
    
    params = {}
    params['page'] = 'cargar.html'
    
    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form'] = form
        
        if form.is_valid():
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']
            dashboard_type = form.cleaned_data['dashboard_type']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            image = form.cleaned_data['image']
            published_date = form.cleaned_data['published_date']
            
            new_dashboard = Dashboards(
                name=name, 
                dashboard_type=dashboard_type, 
                url=url, 
                description=description, 
                status=status, 
                image=image,
                published_date=published_date,
                )
            
            new_dashboard.save()
            
            return redirect(to='main')
    else:
        form = CargarForm()
        params['form'] = form
        
        return render(request, 'tienda/formulario.html', params)


class Usecases(View): 
    template = 'tienda/usecases.html'
    
    def get(self, request):
        params = {}
        params['site_name'] = 'Observability Insights - Ver Dashboards'
        params['page'] = 'usecases.html'
        
        try:
            data = Dashboards.objects.all()
        except Dashboards.DoesNotExist:
            raise Http404
        params['data'] = data
        
        return render(request, self.template, params)

@login_required(redirect_field_name='/' , login_url='/usuarios/login')
def usecase(request, dashboard_id: int):
    template = 'tienda/usecase.html'
    params = {}
    params['site_name'] = 'Observability Insights - Ver Dashboard <id: int>'
    params['page'] = 'usecase.html'
    
    try:
        data = Dashboards.objects.get(pk=dashboard_id)
    except Dashboards.DoesNotExist:
        raise Http404
    params['data'] = data
    
    return render(request, template, params)

@login_required(redirect_field_name='/' , login_url='/usuarios/login')
def scroll(request):
    template = 'tienda/scroll_frame.html'
    params = {}
    params['site_name'] = 'Observability Insights - Animacion con GreenSock'
    params['page'] = 'scroll_frame.html'
    
    
    return render(request, template, params)

def scroll_raw(request):
    template = 'tienda/scroll.html'
    params = {}
    params['site_name'] = 'Observability Insights - Animacion con GreenSock'
    params['page'] = 'scroll.html'
    
    
    return render(request, template, params)

def landing(request):
    template = 'tienda/scroll_frame.html'
    params = {}
    params['site_name'] = 'Observability Insights - Landing Page Template'
    params['page'] = 'scroll_frame.html'
    
    
    return render(request, template, params)

def landing_raw(request):
    template = 'tienda/landing.html'
    params = {}
    params['site_name'] = 'Observability Insights - Animacion con GreenSock'
    params['page'] = 'landing.html'
    
    
    return render(request, template, params)

class SearchDashboard(View):
    def get(self, request):
        result = []
        if request.is_ajax:
            word = request.GET.get('term', '')
            print(word)
            
            dashboard = Dashboards.objects.filter(name__icontains=word)
            
            for d in dashboard:
                data = {}
                data['label'] = d.name
                data['image'] = str(d.image)
                data['description'] = d.description
                result.append(data)
        else:
           result.append('failed') 
            
        mimetype = 'application/json'
        
        return HttpResponse(json.dumps(result), mimetype)

class SearchDashboardAsync(View):
    def get(self, request):
        result = []
        if request.is_ajax:
            word = request.GET['val']
            print(word)
            
            dashboard = Dashboards.objects.filter(name__icontains=word)
            
            for d in dashboard:
                data = {}
                data['label'] = d.name
                data['image'] = str(d.image)
                data['description'] = d.description
                result.append(data)
        else:
           result.append('failed') 
            
        mimetype = 'application/json'
        
        return HttpResponse(json.dumps(result), mimetype)

def search(request):
    template = 'tienda/buscador.html'
    search = SearchDashboardForm()
    params = {}
    params['site_name'] = 'Observability Insights - Busqueda con AJAX'
    params['page'] = 'search.html'
    params['search'] = search
    
    return render(request, template, params)
