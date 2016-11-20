from django.shortcuts import render
from blogperros.models import Perro
from django.shortcuts import render, get_object_or_404
from blogperros.forms import PerroForm
from django.shortcuts import redirect
from blogperros.models import Persona
from blogperros.forms import PersonaForm

# Create your views here.
def listado_perros(request):
    posts = Perro.objects.all()
    return render(request, 'blogperros/listado_perros.html', {'posts': posts})

def detalle_perro(request, pk):
    post = get_object_or_404(Perro, pk=pk)
    return render(request, 'blogperros/detalle_perro.html', {'post': post})

def perro_nuevo(request):
        if request.method == "POST":
            form = PerroForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blogperros.views.editar_perro', pk=post.pk)
        else:
            form = PerroForm()
        return render(request, 'blogperros/editar_perro.html', {'form': form})

def perro_editar(request, pk):
    post = get_object_or_404(Perro, pk=pk)
    if request.method == "POST":
        form = PerroForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogperros.views.detalle_perro', pk=post.pk)
    else:
        form = PerroForm(instance=post)
    return render(request, 'blogperros/editar_perro.html', {'form': form})



def listado_personas(request):
    posts = Persona.objects.all()
    return render(request, 'blogperros/listado_persona.html', {'posts': posts})

def detalle_persona(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    return render(request, 'blogperros/detalle_persona.html', {'post': post})


def persona_nueva(request):
        if request.method == "POST":
            form = PersonaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blogperros.views.detalle_persona', pk=post.pk)
        else:
            form = PersonaForm()
        return render(request, 'blogperros/editar_persona.html', {'form': form})

def editar_persona(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogperros.views.detalle_persona', pk=post.pk)
    else:
        form = PersonaForm(instance=post)
    return render(request, 'blogperros/editar_persona.html', {'form': form})
