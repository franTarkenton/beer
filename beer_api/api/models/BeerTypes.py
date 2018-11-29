'''
Created on Nov. 28, 2018

@author: kjnether
'''

from django.db import models

class BeerTypes(models.Model):
    '''
    beer types model
    '''
    beerTypeId = models.AutoField(primary_key=True)
    beerType = models.CharField(max_length=255, blank=False, unique=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
