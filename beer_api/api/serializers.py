'''
Created on Nov. 28, 2018

@author: kjnether
'''
from rest_framework import serializers
from .models import BeerList
from .models import BeerTypes
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)

class BeerTypesSerializer(serializers.ModelSerializer):
    """Beer type serializer - map to json."""
    
    owner = serializers.ReadOnlyField(source='owner.username')

    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BeerTypes
        fields = ('beerTypeId', 'beerType', 'dateCreated', 'dateModified', 'owner')
        read_only_fields = ('beerTypeId', 'dateCreated', 'dateModified')
        
class BeerListSerializer(serializers.ModelSerializer):
    """Beer list serializer. - map to json
    
    later could set this up so the api defines the foreign key
    relationship using the text value of beerType instead 
    of the primary key. 
    https://stackoverflow.com/questions/22173425/limit-choices-to-foreignkey-in-django-rest-framework
    """
    #beerType = BeerTypesSerializer(read_only=False)
    beerType = serializers.PrimaryKeyRelatedField(
        queryset=BeerTypes.objects.all(),  # @UndefinedVariable
        required=True,
        write_only=False)
    owner = serializers.ReadOnlyField(source='owner.username')
        
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BeerList
        fields = ('beerId', 'beerName', 'beerType', 'dateCreated', 'dateModified', 'owner')
        read_only_fields = ('beerId', 'dateCreated', 'dateModified')
        depth = 1
        
#     def create(self, validated_data):
#         logger.debug(f"validated data: {validated_data}")
#         
#         return BeerList.objects.create(**validated_data)

    def validate_beerType(self, value):
        # to validate beertype
        logger.debug(f"value: {value}")
        return value
    
class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    beerlist = serializers.PrimaryKeyRelatedField(
        many=True, queryset=BeerList.objects.all())  # @UndefinedVariable

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'beerlist')

        
