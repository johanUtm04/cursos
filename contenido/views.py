from django.shortcuts import HttpResponse, render, redirect
from .forms import CursoForm



# Se define una funcion llamada principal y con request le pedimos al navegador que la muestre
def principal(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contenido/principal.html')  # redirige a la misma página
    else:
        form = CursoForm()

    return render(request, 'contenido/principal.html', {'form': form})

def cursos (request): 
    return render (request, "contenido/cursos.html")


def contacto (request): 
    return render (request, "contenido/contacto.html")