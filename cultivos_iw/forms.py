from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['title', 'description', 'weather', 'image', 'quantity', 'difficulty', 'season', 'illumination', 'type']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'weather': 'Clima',
            'quantity': 'Cantidad',
            'difficulty': 'Dificultad',
            'season': 'Estación',
            'illumination': 'Iluminación',
            'type': 'Tipo',
            'image': 'Imagen'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del cultivo'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Detalles y características sobre el cultivo'
            }),
            'weather': forms.Select(attrs={
                'class': 'form-select'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'season': forms.Select(attrs={
                'class': 'form-select'
            }),
            'illumination': forms.Select(attrs={
                'class': 'form-select'
            }),
            'type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }