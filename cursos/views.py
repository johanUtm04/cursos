from django.shortcuts import render, redirect, get_object_or_404 
from .models import Curso  # Model Import
from .forms import CursoForm #Form Import

def principal(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos/principal.html')
    else:
        form = CursoForm()

    return render(request, 'cursos/principal.html', {'form': form})

def cursos (request): 
    cursos = Curso.objects.all()
    return render (request, "cursos/cursos.html", {'cursos': cursos})

#Create a new course
def create_course(request):
    #if the form was send
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid(): #Is the data is valid
            form.save() #the data is saved
            return redirect('principal') #redirected to the list
    else:
        form = CursoForm()
    return render (request, 'cursos/create_curso.html', {'form': form})

#Edit a course
def edit_course(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/edit_curso.html', {'form': form, 'curso': curso})
    
#delete a course 
def delete_course(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')
    return render(request, 'cursos/confirmar_eliminar.html', {'curso': curso})
