from django import forms
from blogpersona.models import Perro

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('nombre', 'color','raza','fecha_nacimiento','imagen')
