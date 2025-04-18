from django.db import models

# Create your models here.

from django.db import models

# Modèle représentant une personne
class Personne(models.Model):
    nom = models.CharField(max_length=100)         # Champ texte pour le nom
    prenom = models.CharField(max_length=100)      # Champ texte pour le prénom
    age = models.IntegerField()                    # Champ numérique pour l'âge
    genre = models.CharField(max_length=10)        # Champ texte pour le genre (M/F/autre)
    adresse = models.CharField(max_length=255)     # Champ texte pour l'adresse

    def __str__(self):
        return f"{self.prenom} {self.nom}"
