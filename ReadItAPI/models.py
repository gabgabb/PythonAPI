from django.db import models

class Communaute(models.Model):
    PRIVE = 'PV'
    PUBLIC = 'PU'
    RESTREINT = 'RE'
    TYPE_COMMU = (
        (PRIVE,'Prive'),
        (PUBLIC,'Public'),
        (RESTREINT,'Restreint'),
    )

    nom = models.CharField(max_length=200, unique=True)
    adherent = models.IntegerField(null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    type_commu = models.CharField(
        max_length=2,
        choices=TYPE_COMMU,
        default=PUBLIC,
    )
