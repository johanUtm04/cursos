from django.shortcuts import HttpResponse, render




# Se define una funcion llamada principal y con request le pedimos al navegador que la muestre
def principal (request): 
    return render (request, "contenido/principal.html")

def cursos (request): 
    return render (request, "contenido/cursos.html")


def contacto (request): 
    return render (request, "contenido/contacto.html")