
from django.shortcuts import render, HttpResponse

# Create your views here.

menu = """<a href="/home/">home</a>
<a href="/cont/">contactanos</a>
    """

def  principal (request):
    contenido="<h1>Hola django</h1>"
    return HttpResponse(menu+contenido)

def contacto (request):
    contenide="""<h2>Contactos</h2>
     <p>Noombre: <input type="text" name="nombre"></p>
    
    <p>Mensaje:</p><p><textarea  cols="50" rows="10"></textarea></p>
    <p><input type="button" value="Enviar" name="enviar"></p>
    """
    return HttpResponse(menu+contenide)

    