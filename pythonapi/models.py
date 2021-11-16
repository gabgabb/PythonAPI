from django.db import models

class CommunauteModel(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=80, blank=False)
    dateCreation = models.DateField(blank=False)
    type = models.CharField(max_length=40, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}:{self.name}:{self.dateCreation},{self.type}"
