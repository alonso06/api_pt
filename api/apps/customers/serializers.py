from rest_framework import serializers
from .models import (Customer, CustomerType)



class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerType
        fields= '__all__' # type: ignore
        read_only_fields = ['created_date, updated_date']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= '__all__' # type: ignore
        read_only_fields = ['created_date, updated_date']
