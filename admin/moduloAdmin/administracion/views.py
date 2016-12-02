from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
#import request
import ssl


def agregarLibro(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'vistas/agregar_libro.html')

def nuevoLibro(request):
	return HttpResponse(request)

def listarLibros(request):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx))
	#opener.addheaders = [('Referer', 'http://software.goodfirmcolombia.co/listar-libros')]
	#datos = opener.open("http://software.goodfirmcolombia.co/listar-libros").read()	
	opener.addheaders = [('Referer', 'http://localhost/software/prueba')]
	datos = opener.open("http://localhost/software/prueba").read()	
	datos = json.loads(datos)
	return HttpResponse(datos['datos'])
	
