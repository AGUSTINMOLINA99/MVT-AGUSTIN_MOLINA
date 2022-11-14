from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")


def datos_familiares(request):

    archivo = open(r"./PRIMERMVT/templates/plantilla.html")

    plantilla = Template(archivo.read())

   
    archivo.close()

    informacion_nombre = ['Nombre: Eduardo',
     'Nombre: Agustin.',
     'Nombre: Juana.',
     'Nombre: Laura.'
    ]

    informacion_edad = ['Edad: 50',
    'Edad: 22',
    'Edad: 50',
    'Edad: 20'
    ]

    datos = {'informacion': informacion_nombre,'Edad': informacion_edad}

  
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)