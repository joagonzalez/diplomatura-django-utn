from django.shortcuts import render

# @login_required(login_url='/accounts/login')
def index(request):
    params = {}
    params['site_name'] = 'Observability Insights - Tienda'
    params['page'] = 'tienda.html'
    
    return render(request, 'tienda/index.html', params)
