from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^/agregar-libro', agregarLibro, name='agregarLibro'),   
    url(r'^/nuevo-libro', nuevoLibro, name='nuevoLibro'),
    url(r'^/editar-libros', editarLibros, name='editarLibros'),
    url(r'^/editar-libro', editarLibro, name='editarLibro'),
    url(r'^/actualizar-libro', actualizarLibro, name='actualizarLibro'),
    url(r'^/eliminar-libro', eliminarLibro, name='eliminarLibro'),
]	