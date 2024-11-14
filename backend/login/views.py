from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
class IniciarSesion(LoginView):
    template_name = 'iniciarsesion.html'
    authentication_form = AuthenticationForm


def Registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Crear el usuario sin guardar aún para añadir el email
            user = form.save(commit=False)
            # Añadir el correo electrónico
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, "Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.")
            return redirect('IniciarSesion')
        else:
            messages.error(request, "Por favor, corrige los errores a continuación.")
    else:
        form = UserCreationForm()
    
    return render(request, 'registrarse.html', {'form': form})

