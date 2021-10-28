from django.db import models

class Communauté(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    adherent = models.IntegerField(null=True)
    cree_le = models.DateTimeField(auto_now_add=True)