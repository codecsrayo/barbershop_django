from django.urls import path
from .views import agregar_cortes, agregar_empleados, eliminar_empleados, listar_empleados, main_page, modificar_empleados, registro, cita,  agregar_cortes, listar_cortes, modificar_cortes, eliminar_cortes, \
    agregar_empleados, listar_empleados, modificar_empleados, eliminar_empleados

urlpatterns = [
	path('', main_page, name='main_page_url'),
 	path('registro/', registro, name='registro'),
  	path('cita/', cita, name='cita'),
	path('agregar-corte/', agregar_cortes, name='agregar_cortes'),
	path('listar-cortes/', listar_cortes, name='listar_cortes'),
	path('modificar-cortes/<id>/', modificar_cortes, name='modificar_cortes'),
	path('eliminar-cortes/<id>/', eliminar_cortes, name='eliminar_cortes'),
 	path('agregar-empleados/', agregar_empleados, name='agregar_empleados'),
	path('listar-empleados/', listar_empleados, name='listar_empleados'),
	path('modificar-empleados/<id>/', modificar_empleados, name='modificar_empleados'),
	path('eliminar-empleados/<id>/', eliminar_empleados, name='eliminar_empleados'),
]