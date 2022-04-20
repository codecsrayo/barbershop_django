from django.urls import path
from .views import agregar_cortes, main_page, registro, cita,  agregar_cortes, listar_cortes, modificar_cortes, eliminar_cortes

urlpatterns = [
	path('', main_page, name='main_page_url'),
 	path('registro/', registro, name='registro'),
  	path('cita/', cita, name='cita'),
	path('agregar-corte/', agregar_cortes, name='agregar_cortes'),
	path('listar-cortes/', listar_cortes, name='listar_cortes'),
	path('modificar-cortes/<id>/', modificar_cortes, name='modificar_cortes'),
	path('eliminar-cortes/<id>/', eliminar_cortes, name='eliminar-cortes'),

]