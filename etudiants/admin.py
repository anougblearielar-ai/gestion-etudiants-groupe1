from django.contrib import admin
from .models import Etudiant, Filiere


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'matricule', 'niveau', 'filiere')
    list_filter = ('filiere', 'niveau')
    search_fields = ('nom', 'prenom', 'matricule')
