from django.db import models

class CommunauteModel(models.Model):

    PUBLIC = 'PU'
    PRIVE = 'PV'
    RESTREINT = 'RT'

    TYPE_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVE,'Prive'),
        (RESTREINT,'Restreint'),
    ]

    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=80, blank=False)
    membre = models.IntegerField(
        default=0,
    )
    dateCreation = models.DateField(blank=False)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=PUBLIC,
    )

    def __str__(self):
        return f"{self.id}:{self.name}:{self.membre}:{self.dateCreation},{self.type}"