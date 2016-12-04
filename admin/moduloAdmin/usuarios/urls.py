from django.conf.urls import url

#from views import *
from views import RegistroUsuario

urlpatterns = [
    url(r'^/', RegistroUsuario.as_view(), name='registrar'),       
]	