from django.db import models
from .BeerTypes import BeerTypes


class BeerList(models.Model):
    '''
    beer list model
    '''
    beerId = models.AutoField(primary_key=True)
    beerName = models.CharField(max_length=255, blank=False, unique=True)
    beerType = models.ForeignKey(BeerTypes, on_delete=models.CASCADE,
                                   related_name='beerTypeRel',
                                   to_field='beerTypeId', null=False,
                                   blank=False, editable=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    
#     @property
#     def beerType_name(self):
#         return self.beerType.beerType

    
