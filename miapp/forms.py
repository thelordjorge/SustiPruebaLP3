from django import forms
from django.core import validators

class FormRegion(forms.Form):
    name = forms.CharField(
        label="Región",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título',
                'class': 'titulo_form_articulo'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El título tiene caracteres inválidos','titulo_invalido')
        ]
    )

    cases = forms.CharField(
        label="Casos",
        widget=forms.TextInput,
        validators=[
            validators.MaxLengthValidator(150,'Superaste el límite de caracteres')
        ]        
    )
    deaths = forms.CharField(
        label="Muertes",
        widget=forms.TextInput,
        validators=[
            validators.MaxLengthValidator(150,'Superaste el límite de caracteres')
        ]        
    )
    lethality = forms.CharField(
        label="Letalidad",
        widget=forms.TextInput,
        validators=[
            validators.MaxLengthValidator(150,'Superaste el límite de caracteres')
        ]        
    )
   
    cases.widget.attrs.update({
        'placeholder': 'Ingrese el numero de casos',
        'class': 'cases_form_region',
        'id':'cases_form'
    })

    deaths.widget.attrs.update({
        'placeholder': 'Ingrese el numero de muertes',
        'class': 'deaths_form_region',
        'id':'deaths_form'
    })

    lethality.widget.attrs.update({
        'placeholder': 'Ingrese el numero de letalidad',
        'class': 'lethality_form_regin',
        'id':'lethality_form'
    })


    