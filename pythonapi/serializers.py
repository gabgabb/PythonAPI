from rest_framework import serializers
from .models import CommunauteModel

class CommunauteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommunauteModel
        fields = ['id','name','membre','dateCreation','type']