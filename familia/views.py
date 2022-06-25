from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Familiares

# Create your views here.
def index(request):
    return render(request, 'index.html')

def volver(request):
    return render(request, 'index.html')

def cargar_familiares(request):
        
    padre = Familiares(nombre='Nestor', edad=61, anio_nacimiento='1961-06-20')
    madre = Familiares(nombre='Sandra', edad=60, anio_nacimiento='1962-02-26')
    hermano = Familiares(nombre='Octavio', edad=30, anio_nacimiento='1992-02-21')
    
    padre.save()
    madre.save()
    hermano.save()
    
    return render(request, 'carga_familia.html')
    
def listar_familiares(request):

    template = loader.get_template('familia.html')

    listar_familiares = Familiares.objects.all()

    render = template.render({'listar_familiares': listar_familiares})

    return HttpResponse(render)