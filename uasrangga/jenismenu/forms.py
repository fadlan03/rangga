from django.forms import ModelForm
from django import forms
from menu_app.models import *

class FormPeta(ModelForm):
    class Meta:
        model = Peta
        fields = '__all__'

        widgets = {
            'no' : forms.NumberInput({'class':'form-control', 'placeholder':'no', 'required':'required'}),
            'nama_lokasi' : forms.TextInput({'class':'form-control', 'placeholder':'peta', 'required':'required'}),
            'titik_koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'titik koordinat', 'required':'required'}),
            'deskripsi' : forms.TextInput({'class':'form-control', 'placeholder':'deskripsi', 'required':'required'}),
        }