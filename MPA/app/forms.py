from django import forms
from .models import Ciudad

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'