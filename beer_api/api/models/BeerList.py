
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    owner = models.ForeignKey('auth.User',
                              related_name='beerList', 
                              on_delete=models.CASCADE)
                              

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    
#     @property
#     def beerType_name(self):
#         return self.beerType.beerType

# creates user token when new user is added.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
