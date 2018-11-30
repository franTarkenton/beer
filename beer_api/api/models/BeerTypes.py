'''
Created on Nov. 28, 2018

@author: kjnether
'''

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class BeerTypes(models.Model):
    '''
    beer types model
    '''
    beerTypeId = models.AutoField(primary_key=True)
    beerType = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',
                              related_name='beerTypes', 
                              on_delete=models.CASCADE) 
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return f"{self.beerType}"
    
# creates user token when new user is added.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
