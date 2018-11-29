'''
Created on Nov. 28, 2018

@author: kjnether
'''
from rest_framework import serializers
from .models import BeerList
from .models import BeerTypes

import logging
logger = logging.getLogger(__name__)

class BeerTypesSerializer(serializers.ModelSerializer):
    """Beer type serializer - map to json."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BeerTypes
        fields = ('beerTypeId', 'beerType', 'dateCreated', 'dateModified')
        read_only_fields = ('beerTypeId', 'dateCreated', 'dateModified')
        
class BeerListSerializer(serializers.ModelSerializer):
    """Beer list serializer. - map to json"""
    #beerType = BeerTypesSerializer(read_only=False)
    beerType = serializers.PrimaryKeyRelatedField(
        queryset=BeerTypes.objects.all(),
        required=True,
        write_only=False)

        
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BeerList
        fields = ('beerId', 'beerName', 'beerType', 'dateCreated', 'dateModified')
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

        
