
import datetime
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render



class Persona:
  def __init__(self, nombre, apellido):
    
    self.nombre = nombre
    
    self.apellido = apellido

def saludo(request): # Primera Vista
  
  p1 = Persona("Profesor Jonathan", "Patiño")
 
  #nombre = "Jonathan"
  #apellido = "Patiño"
  
  temasdelcurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

  ahora = datetime.datetime.now()

  #doc_externo=open("/home/jonathan/mytestsite/mytestsite/plantillas/mipantilla.html")
  #plt = Template(doc_externo.read())
  #doc_externo.close()
  
  #doc_externo = get_template('mipantilla.html')
  
  #ctx = Context({"nombre_persona":p1.nombre,"segundo_nombre":"Armando" ,"apellido_persona":p1.apellido.upper, "momento_actual":ahora,"temas":temasdelcurso})
  #documento = doc_externo.render({"nombre_persona":p1.nombre,"segundo_nombre":"Armando" ,"apellido_persona":p1.apellido.upper, "momento_actual":ahora,"temas":temasdelcurso})
  #return HttpResponse(documento)
  return render(request, "miplantilla.html",{"nombre_persona":p1.nombre,"segundo_nombre":"Armando" ,"apellido_persona":p1.apellido.upper, "momento_actual":ahora,"temas":temasdelcurso})


def cursoC(request):

  fecha_actual = datetime.datetime.now()
  return render(request, "CursoC.html",{"dame_fecha":fecha_actual})

def cursoCss(request):

  fecha_actual = datetime.datetime.now()
  return render(request, "cursoCss.html",{"dame_fecha":fecha_actual})



def despedida(request): # Segunda Vista
  return HttpResponse("Chau Cande te amo mucho")

def damefecha(request):
  fecha_actual = datetime.datetime.now()
  documento = """<html>
  <body>
  <h2 style = "color:red">
    Fecha y hora actuales %s
  </h2>
  </body>
  </html>"""% fecha_actual
  return HttpResponse(documento)

def calculaEdad(request, edad , anio):
  
  periodo = anio-2019
  edadFutura = edad + periodo
  documento = """<html>
  <body>
  <h2 style = "color:red">
    En el año %s tendrás %s años
  </h2>
  </body>
  </html>"""%(anio, edadFutura)
  return HttpResponse(documento)