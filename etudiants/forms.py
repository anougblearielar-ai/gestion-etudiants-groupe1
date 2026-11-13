
from django import forms
from .models import Etudiant


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'matricule', 'niveau', 'filiere']

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l’étudiant'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom de l’étudiant'
            }),
            'matricule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Matricule'
            }),
            'niveau': forms.Select(attrs={
                'class': 'form-control'
            }),
            'filiere': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
