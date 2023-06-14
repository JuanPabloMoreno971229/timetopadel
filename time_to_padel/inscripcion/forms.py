from tkinter import Label
from django import forms
from django.forms import widgets 
from .models import inscripcion


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = inscripcion
        fields = '__all__'
        widgets = {
            'name_1': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre jugador 1'}),
            'lastname_1' : forms.TextInput(attrs={'type': 'text','class':'form-control','placeholder':'Apellido jugador 1', 'name':"name"}),
            'phone_1' : forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono jugador 1'}),
            'mail_1' : forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail juagdor 1'}),
            'name_2' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre jugador 2'}),
            'lastname_2' : forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido jugador 2'}),
            'phone_2' : forms.TextInput(attrs={'class':'form-control','placeholder':'Teléfono jugador 2'}),
            'mail_2' : forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail juagador 2'}),
            'category' : forms.Select(attrs={'class':'form-control','placeholder':'Categoría'}),
            'level' : forms.Select(attrs={'class':'form-control','placeholder':'Nivel'}),

        }
        labels = {'procedure': '','name': '', 'mail': '', 'phone': '', 'message': ''}
        labels = {'name_1': '', 'lastname_1': '', 'phone_1': '', 'mail_1': '', 'name_2':'', 'lastname_2': '', 'phone_2': '', 'mail_2': '', 'category': '', 'level': ''}
    