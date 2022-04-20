from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from .forms import CustomUserCretionForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator 
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Catalogo, Citas
from .forms import CitasForm, CatalogoForm

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
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mesaje"] = "Cita realizada"
            return redirect(to="main_page_url")
        else:
            data["form"] = formulario
            data["mesaje"] = "No fuesposible guardar el contacto.."
    
    return render(request, 'barber_app/cita.html', data)






#@permission_required('barber_app.add_producto')
def agregar_cortes(request):
    
    data = {
        'form': CatalogoForm()
    }
    
    if request.method == 'POST':
        formulario = CatalogoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Catalogo agregado correctamente.")
        else:       
            data["form"] = formulario
            data["mesaje"] = "No fuesposible guardar el contacto.."
    return render(request, 'barber_app/catalogo/agregar.html', data)

#@permission_required('barber_app.view_producto')
def listar_cortes(request):
    cortes = Catalogo.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(cortes, 5)
        cortes = paginator.page(page)
        
    except:
        raise Http404
    
    
    data = {
        'entity': cortes,
        'paginator': paginator
    }
    
    return render(request, 'barber_app/catalogo/listar.html', data)

#@permission_required('barber_app.change_producto')
def modificar_cortes(request, id):
    producto = get_object_or_404(Catalogo, id=id)
    
    data={
        'form': CatalogoForm(instance=producto)
    }
    
    if request.method =='POST':
        formulario = CatalogoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_cortes")
        data['form'] = formulario
        
    return render(request, 'barber_app/catalogo/modificar.html', data)

#@permission_required('barber_app.delete_producto')
def eliminar_cortes(request, id):
    corte = get_object_or_404(Catalogo, id=id)
    corte.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_cortes")

