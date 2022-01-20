import datetime
from urllib import response
from django.http import HttpResponse
def saludo(request): # Primera Vista
  documento = """<html>
  <body><h1 style = "color:green">Cande te amo mucho yo</h1>
  </body>
  </html>"""
  return HttpResponse(documento)

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