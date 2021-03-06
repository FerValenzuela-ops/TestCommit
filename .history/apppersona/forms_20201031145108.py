from django import forms
from django.db import models
from django.forms import ModelForm, Textarea
from django.forms.widgets import TextInput

from .models import Persona
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm



class FormularioPersona(forms.ModelForm) :
    
    class Meta:
        model =  Persona
        fields = ('nombre' ,'apellido', 'email' ,'celular', 'usuario', 'region' , 'contraseña', 'contraseñaconfirmar')
        widgets = {
          'nombre': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;', 'id': 'email'}),
          'apellido': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
          'email': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
          'celular': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
          'usuario': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
          'contraseña': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
          'contraseñaconfirmar': Textarea(attrs={'rows':1, 'cols':30, 'style':'resize:none;'}),
        }
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'email': _('Correo Electronico'),
            'celular': _('Numero Telefonico'),
            'usuario': _('Usuario'),
            'region': _('Region'),
            'contraseña': _('Contraseña'),
            'contraseñaconfirmar': _('Confirmar Contraseña'),
        }

        
               

        """help_texts = {
            'nombre': _('Ingrese su nombre.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("El nombre excede el limite de caracteres."),
            },
        }"""

        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    region = forms.CharField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
     

        

       