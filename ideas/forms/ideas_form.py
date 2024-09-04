# from django import forms
# from ideas.models import Ideas

# class IdeasForm(forms.ModelForm):
#     class Meta:
#         model = Ideas
#         fields = [
#             'title',
#             'description',
#             'key_words',
#             'resources',
#             'created_at',
#             'innovation_type',
#             'innovation_focus',
#             'file',
#         ]

#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#             'created_at': forms.DateInput(format='%d/%m/%Y', attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Selecciona una fecha',
#                 'type': 'date'
#             }),
#         }


        
#         labels = {
#             'created_at' : 'Fecha',
#             # 'created_by' : 'Responsable',
#             'title': 'Título',
#             'description': 'Descripción',
#             'key_words': 'Palabras clave',
#             'resources': 'Recursos requeridos',
#             'innovation_type': 'Tipo de innovación',
#             'innovation_focus': 'Foco de innovación',
#             'file': 'Archivo'
            
#         }


# ideas/forms.py
from django import forms

class IdeasForm(forms.Form):
    title = forms.CharField(
        max_length=200, 
        label='Título', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la idea'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Proporcione una descripción detallada de la idea'}),
        label='Descripción'
    )
    key_words = forms.CharField(
        max_length=255, 
        required=False, 
        label='Palabras clave', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Palabras clave relacionadas con la idea'})
    )
    resources = forms.CharField(
        max_length=255, 
        required=False, 
        label='Recursos', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recursos necesarios para la implementación'})
    )
    innovation_type = forms.CharField(
        max_length=50, 
        label='Tipo de Innovación', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el tipo de innovación'})
    )
    innovation_focus = forms.CharField(
        max_length=50, 
        label='Foco de Innovación', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el foco de innovación'})
    )
    # created_at = forms.DateField(
    #     widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    #     label='Fecha de Creación'
    # )
    created_by = forms.CharField(
        max_length=100, 
        label='Creado por', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el usuario que creó esta idea'})
    )
    file = forms.FileField(
        required=False, 
        label='Archivo', 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
