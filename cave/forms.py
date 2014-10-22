#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from cave.models import Bouteille

"""
 Use to construct a add bottle form
"""
class addBouteilleForm(forms.Form):
    idBouteille = forms.IntegerField(min_value=0,widget=forms.HiddenInput())
    nbBouteille = forms.IntegerField(min_value=1,max_value=100)
    prixUnitaire = forms.DecimalField(max_digits=8,decimal_places=2,help_text="Prix de la bouteille en euros (€)")
    gardeMin = forms.IntegerField(min_value=1, help_text="Garde minimale de la bouteille")
    gardeMax = forms.IntegerField(min_value=1, help_text="Garde maximale de la bouteille")

