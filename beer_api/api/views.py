'''
Created on Nov. 28, 2018

@author: kjnether
'''

from rest_framework import generics
from .serializers import BeerTypesSerializer
from .serializers import BeerListSerializer
from .models import BeerTypes
from .models import BeerList
import logging

logger = logging.getLogger(__name__)

class CreateBeerTypeView(generics.ListCreateAPIView):
    """defines the create behavior for beer types."""
    queryset = BeerTypes.objects.all()  # @UndefinedVariable
    serializer_class = BeerTypesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        logger.debug(f"type serializer: {serializer}")
        # don't create it if it already exists
        queryset = BeerTypes.objects.all()  # @UndefinedVariable
        logger.debug(f"queryset: {queryset} ")
        serializer.save()
        
class CreateBeerListView(generics.ListCreateAPIView):
    queryset = BeerList.objects.all()  # @UndefinedVariable
    serializer_class = BeerListSerializer
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        logger.debug(f'serializer: {serializer}')
        
        serializer.save()
        
        

