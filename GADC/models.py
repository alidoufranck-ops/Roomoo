from django.db import models
from django.utils import timezone
# Create your models here.
class Formulaire(models.Model):
    demandeur = models.CharField(max_length=100)
    demande = models.CharField(max_length=100)
    details = models.TextField(max_length= 500)
    statut = [('En attente', 'En attente'),              ('En cours', 'En cours'),
              ('Terminé', 'Terminé')]
    statut = models.CharField(max_length=20, choices=statut, default='En attente')
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.demandeur} - {self.statut}"