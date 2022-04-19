from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Catalogo, Citas



class CustomUserCretionForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class CatalogoForm(forms.ModelForm):
        class Meta:
            model = Catalogo
            fields = ['nombre', 'precio', 'imagen']
            


class CitasForm(forms.ModelForm):
        class Meta:
            model = Citas
            fields = ['nombre_cliente', 'corte', 'empleado', 'precio']
            