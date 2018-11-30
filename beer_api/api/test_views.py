'''
Created on Nov. 28, 2018

@author: kjnether
'''
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.models.BeerTypes import BeerTypes
from api.models.BeerList import BeerList
from django.contrib.auth.models import User

import logging

class ViewTestBeerTypeCreate(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.logger = logging.getLogger(__name__)
        
        self.user = User.objects.create(username="Lebowski")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.beerTypeData = {'beerType': 'India Pale Ale', 
                             'beerTypeId': 1,
                             'owner':self.user.id}
        self.beerListData = {'beerName': 'Red Racer',
                        'beerId': 1, 
                        'beerType': self.beerTypeData['beerTypeId'], 
                        'owner':self.user.id}


    def test_api_create_BeerType(self):
        """Can api create beertype."""
        self.response = self.client.post(
            reverse('CreateBeerTypeView'),
            self.beerTypeData,
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_create_BeerList(self):
        response = self.client.post(
            reverse('CreateBeerTypeView'),
            self.beerTypeData,
            format="json")
        beerType = response.content
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        beerTypeType = type(beerType) 
        self.logger.debug(f"response: {beerType}  {beerTypeType}")
        

        response = self.client.post(
            reverse('CreateBeerListView'),
            self.beerListData,
            format="json")
          
        self.logger.debug("test test test")
        self.logger.debug(f"self.response: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#                 
#     def test_api_can_get_a_bucketlist(self):
#         """Test the api can get a given bucketlist."""
#         bucketlist = Bucketlist.objects.get()
#         response = self.client.get(
#             reverse('details',
#             kwargs={'pk': bucketlist.id}), format="json")
# 
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, bucketlist)

        
        
        
        
# class ViewTestBeerListCreate(TestCase):
#     """Test suite for the api views."""
# 
#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.logger = logging.getLogger(__name__)
# 
#         self.client = APIClient()
#         self.beerTypeData = {'beerType': 'India Pale Ale5', 
#                              'beerTypeId': 5}
#         #self.response = self.client.post(
#         #    reverse('CreateBeerTypeView'),
#         #    self.beerTypeData,
#         #    format="json")
#         #print(f'self.response {self.response.content}')
#         # now create the beer list item with the relationship back to 
#         # this item.
#         self.beerListData = {'beerName': 'Red Racer',
#                              'beerId': 1, 
#                              'beerType': self.beerTypeData }
#         
#         self.response = self.client.post(
#             reverse('CreateBeerListView'),
#             self.beerListData,
#             format="json")
#         self.logger.debug("test test test")
#         self.logger.debug(f"self.response: {self.response.content}")
#         
# 
#     def test_api_create_BeerList(self):
#         """Can api create beerlist"""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         
    
