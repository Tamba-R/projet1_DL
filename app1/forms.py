from django import forms
from .models import Personne

# Formulaire basé sur le modèle Personne
class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'age', 'genre', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'placeholder': 'Prénom'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Âge'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
        }