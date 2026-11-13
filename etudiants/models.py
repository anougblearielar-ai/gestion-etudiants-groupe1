from django.db import models


class Filiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "Filière"
        verbose_name_plural = "Filières"

    def __str__(self):
        return self.nom


class Etudiant(models.Model):
    NIVEAUX = [
        ("L1", "Licence 1"),
        ("L2", "Licence 2"),
        ("L3", "Licence 3"),
        ("M1", "Master 1"),
        ("M2", "Master 2"),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)
    niveau = models.CharField(max_length=2, choices=NIVEAUX)
    filiere = models.ForeignKey(
        Filiere,
        on_delete=models.PROTECT,
        related_name="etudiants",
    )

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "Étudiant"

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matricule})"
    
