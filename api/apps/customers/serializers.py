from rest_framework import serializers
from models import (Customer, CustomerType)



class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model: CustomerType
        fields: '__all__' # type: ignore

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model: CustomerType
        fields: '__all__' # type: ignore
