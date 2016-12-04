from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json
#import request
import ssl
from models import Servicio


def agregarLibro(request):
	servicio = Servicio()
	categorias = servicio.pedir('listar-categorias')
	contexto = {'categorias' : categorias}
	return render(request, 'administrar/agregar_libro.html', contexto)

def nuevoLibro(request):
	datosEnviar = {
		'categoria' : request.POST['categoria'],
		'titulo' : request.POST['titulo'],
		'autor' : request.POST['autor'],
		'fecha' : request.POST['fecha'],
		'imagen' : request.FILES['imagen'],
		'descripcion' : request.POST['descripcion'],
		'precio' : request.POST['precio']
		}
	servicio = Servicio()
	respuesta = servicio.enviar('agregar-libro', datosEnviar)

	categorias = servicio.pedir('listar-categorias')
	contexto = {'categorias' : categorias, 'respuesta' : respuesta}
	return render(request, 'administrar/agregar_libro.html', contexto)


def editarLibros(request):
	servicio = Servicio()
	libros = servicio.pedir('editar-libros')
	contexto = {'libros' : libros}
	return render(request, 'administrar/editar_libros.html', contexto)


def editarLibro(request):
	servicio = Servicio()
	libro = servicio.pedir('pedir-libro/' + request.GET['id'])
	categorias = servicio.pedir('listar-categorias')
	return render(request, 'administrar/editar.html', {'libro' : libro, 'categorias' : categorias})

def listarLibros(request):
	servicio = Servicio()
	libros = servicio.pedir('listar-libros')
	contexto = {'libros' : libros}
	return render(request, 'administrar/editar_libros.html', contexto)	


def actualizarLibro(request):
	datosEnviar = {
		'id' : request.POST['id'],
		'categoria' : request.POST['categoria'],
		'titulo' : request.POST['titulo'],
		'autor' : request.POST['autor'],
		'fecha' : request.POST['fecha'],
		'descripcion' : request.POST['descripcion'],
		'precio' : request.POST['precio']
		}
	servicio = Servicio()
	respuesta = servicio.enviar2('actualizar-libro', datosEnviar)

	libros = servicio.pedir('editar-libros')
	contexto = {'libros' : libros}
	return render(request, 'administrar/editar_libros.html', contexto)

def eliminarLibro(request):
	servicio = Servicio()
	
	libro = servicio.pedir('eliminar-libro/' + request.GET['id'])

	libros = servicio.pedir('listar-libros')
	contexto = {'libros' : libros}
	return render(request, 'administrar/editar_libros.html', contexto)

