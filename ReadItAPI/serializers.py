from rest_framework import serializers
from .models import Communaute

class CommunauteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communaute
        fields = ['id','nom','adherent','cree_le','type_commu']