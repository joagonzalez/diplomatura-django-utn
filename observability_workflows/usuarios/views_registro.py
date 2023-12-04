from django.shortcuts import render
from django.shortcuts import redirect
from usuarios.forms import CreateUserForm



# Create your views here.
def register(request):
    params = {}
    params['site_name'] = 'Observability Insights Register page Usuarios'
    params['page'] = 'register.html'
    
    form = CreateUserForm()
    params['form'] = form
    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(to='login')
        
    return render(request, 'usuarios/register.html', params)
