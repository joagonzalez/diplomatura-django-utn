from django.shortcuts import render
from django.contrib.auth import logout as native_logout



# Create your views here.
def logout(request):
    params = {}
    params['site_name'] = 'Observability Insights Logout page Usuarios'
    params['page'] = 'logout.html'
    
    native_logout(request=request)
    return render(request, 'usuarios/login.html', params)
