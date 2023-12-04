from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as native_login



def login(request):
    params = {}
    params['site_name'] = 'Observability Insights Login page Usuarios'
    params['page'] = 'login.html'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
            params['login_status'] = 'success'
            native_login(request, user)
            return redirect(to='main')
        else:
            params['login_status'] = 'failed'
            return render(request=request, template_name='usuarios/login.html', context=params)
    
    return render(request, 'usuarios/login.html', params)
