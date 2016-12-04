from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import urllib
import json
#import request
import ssl
import base64

class Servicio:
	

	def pedir(self, url):
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx))		
		#opener.addheaders = [('Referer', 'http://localhost/software/prueba')]
		#datos = opener.open("http://localhost/software/prueba").read()	
		opener.addheaders = [('Referer', 'http://software.goodfirmcolombia.co/' + url)]
		datos = opener.open("http://software.goodfirmcolombia.co/" + url).read()	
		datos = json.loads(datos)
		return datos


	def enviar(self, url, parametros):
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx))		
		parametros['imagen'] = base64.b64encode(parametros['imagen'].read())
		datosEnviar = urllib.urlencode(parametros)
		#datosEnviar = urllib.urlencode(encoded_image)
		#datosEnviar = (parametros['imagen'])
		opener.addheaders = [('Referer', 'http://software.goodfirmcolombia.co/' + url)]
		datosRespuesta = opener.open("http://software.goodfirmcolombia.co/" + url, datosEnviar).read()	
		datosRespuesta = json.loads(datosRespuesta)
		return datosRespuesta



	def enviar2(self, url, parametros):
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx))		
		datosEnviar = urllib.urlencode(parametros)
		opener.addheaders = [('Referer', 'http://software.goodfirmcolombia.co/' + url)]
		datosRespuesta = opener.open("http://software.goodfirmcolombia.co/" + url, datosEnviar).read()	

		datosRespuesta = json.loads(datosRespuesta)
		return datosRespuesta
