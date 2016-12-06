from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import *

urlpatterns = [
	url(r'^$', login_required(editarLibros), name='/'),	
    url(r'^/agregar-libro', login_required(agregarLibro), name='agregarLibro'),   
    url(r'^/nuevo-libro', login_required(nuevoLibro), name='nuevoLibro'),
    url(r'^/editar-libros', login_required(editarLibros), name='editarLibros'),
    url(r'^/editar-libro', login_required(editarLibro), name='editarLibro'),
    url(r'^/actualizar-libro', login_required(actualizarLibro), name='actualizarLibro'),
    url(r'^/eliminar-libro', login_required(eliminarLibro), name='eliminarLibro'),
    url(r'^/ver-clientes', login_required(verClientes), name='verClientes'),
    url(r'^/ver-ventas', login_required(verVentas), name='verVentas'),
    url(r'^/nueva-categoria', login_required(nuevaCategoria), name='nuevaCategoria'),
]	