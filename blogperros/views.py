from django.shortcuts import render
from blogperros.models import Perro
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listado_perros(request):
    posts = Perro.objects.all()
    return render(request, 'blogperros/listado_perros.html', {'posts': posts})

def detalle_perro(request, pk):
    post = get_object_or_404(Perro, pk=pk)
    return render(request, 'blogperros/detalle_perro.html', {'post': post})
