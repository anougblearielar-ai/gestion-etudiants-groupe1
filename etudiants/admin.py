from django.contrib import admin
from .models import Filiere, Etudiant


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")
    search_fields = ("nom",)


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("matricule", "nom", "prenom", "niveau", "filiere")
    list_filter = ("filiere", "niveau")
    search_fields = ("nom", "prenom", "matricule")
