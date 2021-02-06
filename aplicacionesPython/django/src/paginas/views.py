from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(request.user, args, kwargs)
    # return HttpResponse("<h1> Hello World </h1>") # string de código HTM
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    mi_contexto = {
        "titulo": "sobre nosotros",
        "mi_texto": "Esto es sobre nosotros",
        "mi_numero": 123,
        "mi_lista": [123, 456, 789, 'abc'],
        "es_verdad": True
    }
    return render(request, "about.html", mi_contexto)