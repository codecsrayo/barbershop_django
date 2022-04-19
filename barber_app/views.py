from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from .forms import CustomUserCretionForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Catalogo, Citas
from .forms import CitasForm

def main_page(request):
    cortes = Catalogo.objects.all()
    
    data = {
        'corte':cortes
    }
    
    return render(request, 'barber_app/index.html', data)
	

def registro(request):
    
    data = {
        'form': CustomUserCretionForm()
    }
    
    if request.method =='POST':
        
        formulario = CustomUserCretionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="main_page_url")
        data['form'] = formulario
        
    return render(request, 'registration/registro.html', data)



def cita(request):
    
    data = {
        'form': CitasForm()
    }
    
    
    if request.method == 'POST':
        formulario = CitasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mesaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            data["mesaje"] = "No fuesposible guardar el contacto.."
    
    return render(request, 'barber_app/cita.html', data)