from requests import Request
from django.shortcuts import render, redirect
from tienda.forms import CargarForm
from dashboards.models import Dashboards
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def index(request: Request):
    params = {}
    params['site_name'] = 'Observability Insights - Tienda'
    params['page'] = 'tienda.html'
    
    return render(request, 'tienda/index.html', params)


def cargar_imagen(request: Request):
    
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
            
            return redirect(to='index')
    else:
        form = CargarForm()
        params['form'] = form
        
        return render(request, 'tienda/formulario.html', params)