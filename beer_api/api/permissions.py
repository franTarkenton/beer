'''
Created on Nov 29, 2018

@author: kjnether
'''
from rest_framework.permissions import BasePermission
from .models import BeerList
from .models import BeerTypes


class IsOwner(BasePermission):
    """Limiting access to data based on permissions"""

    def has_object_permission(self, request, view, obj):
        """only allow record owner to edit."""
        if isinstance(obj, BeerList):
            return obj.owner == request.user
        if isinstance(obj, BeerTypes):
            return obj.owner == request.user
        return obj.owner == request.user