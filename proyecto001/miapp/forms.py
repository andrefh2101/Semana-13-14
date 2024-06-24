from django import forms
from django.core import validators
class FormArticulo(forms.Form):
    titulo = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título',
                'class': 'titulo_form_articulo'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El título es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El título tiene caracteres inválidos','titulo_invalido')         
        ]    
    )

    # Usar CharField para generar un campo de texto normal
    contenido = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20,'Superaste el límite de caracteres')
        ]
    )


