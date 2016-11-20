from django import forms
from blogperros.models import Perro, Persona

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('nombre', 'color','raza','fecha_nacimiento','imagen')


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dpi', 'nombre','apellido','foto')
