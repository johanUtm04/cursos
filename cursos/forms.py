from django import forms 
from .models import Curso

class CursoForm (forms.ModelForm):
    class Meta:
        model = Curso
        fields =['nombre', 'descripcion', 'duracion', 'precio', 'disponible', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms. Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control',}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    