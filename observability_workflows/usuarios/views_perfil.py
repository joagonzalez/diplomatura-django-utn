from django.shortcuts import render


# Create your views here.
def profile(request):
    params = {}
    params['site_name'] = 'Observability Insights Profile page Usuarios'
    params['page'] = 'profile.html'
    
    return render(request, 'usuarios/profile.html', params)
