from rest_framework import serializers
from . models import *

class products_serializers(serializers.ModelSerializer):
    class Meta:
        model=products_2
        fields='__all__'