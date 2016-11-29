from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^/agregar-libro', agregarLibro, name='agregarLibro'),   
    url(r'^/nuevo-libro', nuevoLibro, name='nuevoLibro'),   
]