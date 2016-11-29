from django.shortcuts import render
from django.http import HttpResponse


def agregarLibro(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'vistas/agregar_libro.html')

def nuevoLibro(request):
	return HttpResponse(request)
