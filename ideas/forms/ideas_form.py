from django import forms
from ideas.models import Ideas

class IdeasForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = [
            'title',
            'description',
            'key_words',
            'resources',
            'created_at',
            'innovation_type',
            'innovation_focus',
            'file',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'created_at': forms.DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona una fecha',
                'type': 'date'
            }),
        }


        
        labels = {
            'created_at' : 'Fecha',
            # 'created_by' : 'Responsable',
            'title': 'Título',
            'description': 'Descripción',
            'key_words': 'Palabras clave',
            'resources': 'Recursos requeridos',
            'innovation_type': 'Tipo de innovación',
            'innovation_focus': 'Foco de innovación',
            'file': 'Archivo'
            
        }
