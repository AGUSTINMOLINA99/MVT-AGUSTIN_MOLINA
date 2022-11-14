from django.http import HttpResponse

from MVT_ENTREGA.models import familia1

# Create your views here.

def listado_de_familia(request):
    listado = familia1.objects.all()

    Vista = ""
    for FAMILIA in listado:
        Vista += f"({FAMILIA.nombre},{FAMILIA.edad})" + " | "

    return HttpResponse(Vista)
