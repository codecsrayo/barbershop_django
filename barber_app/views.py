from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from .forms import CustomUserCretionForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Catalogo

def main_page(request):
    cortes = Catalogo.objects.all()
    
    data = {
        'corte':cortes
    }
    
    return render(request, 'barber_app/index.html', data)
	
# def all_news_page(request):
# 	all_news = News.objects.all()
# 	return render(request, 'barber_app/news.html', {'all_news': all_news})
	
# def price_page(request):
# 	return render(request, 'barber_app/price.html')

# def shop_page(request):
# 	return render(request, 'barber_app/shop.html')

# def item_page(request):
# 	return render(request, 'barber_app/item.html')

# class NewsDetail(View):
# 	def get(self, request, slug):
# 		news = get_object_or_404(News, slug__iexact=slug)
# 		return render(request, 'barber_app/news_detail.html', {'news': news})



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