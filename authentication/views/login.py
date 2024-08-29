from django.shortcuts import render, redirect
from authentication.forms.login_form import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            # Simulación de inicio de sesión
            request.session['username'] = username

            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
