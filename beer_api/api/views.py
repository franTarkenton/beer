'''
Created on Nov. 28, 2018

@author: kjnether
'''

from rest_framework import generics
from rest_framework import permissions
from .serializers import BeerTypesSerializer
from .serializers import BeerListSerializer
from .serializers import UserSerializer
from .models import BeerTypes
from .models import BeerList
from .permissions import IsOwner
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class CreateBeerTypeView(generics.ListCreateAPIView):
    """defines the create behavior for beer types."""
    queryset = BeerTypes.objects.all()  # @UndefinedVariable
    serializer_class = BeerTypesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)


    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        logger.debug(f"type serializer: {serializer}")
        # don't create it if it already exists
        queryset = BeerTypes.objects.all()  # @UndefinedVariable
        logger.debug(f"queryset: {queryset} ")
        serializer.save(owner=self.request.user)
        
class BeerTypesDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView  handles the http GET, PUT and DELETE requests."""
    queryset = BeerTypes.objects.all()  # @UndefinedVariable
    serializer_class = BeerTypesSerializer
    
class BeerListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView  handles the http GET, PUT and DELETE requests."""
    queryset = BeerList.objects.all()  # @UndefinedVariable
    serializer_class = BeerListSerializer

        
class CreateBeerListView(generics.ListCreateAPIView):
    queryset = BeerList.objects.all()  # @UndefinedVariable
    serializer_class = BeerListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        logger.debug(f'serializer: {serializer}')
        
        serializer.save(owner=self.request.user)
        
        
class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

