from django import forms # on
from .models import Formulaire # on importe la table creer dans models

class RegisterFormulaireForm(forms.ModelForm):
    #creation de la class
    class Meta :
        model = Formulaire # on met le pointeur sur ce models
        fields = ['demandeur','demande','details'] # les champs a aoutés