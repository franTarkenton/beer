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
        beerTypes = BeerTypes.objects.get()
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
        
    def test_api_get_BeerTypes(self):
        """Test the api can get a given beertypes."""
        # make sure a beer type record exists
        self.test_api_create_BeerType()
        beerTypes = BeerTypes.objects.get()
        self.logger.debug(f"beertypes: {beerTypes}, {beerTypes.beerTypeId}")
        response = self.client.get(
            reverse('BeerTypesDetails',
            kwargs={'pk': beerTypes.beerTypeId}), format="json")
  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, beerTypes)
        
    def test_api_update_BeerTypes(self):
        """Test api can update a beertypes."""
        self.test_api_create_BeerType()
        beerTypes = BeerTypes.objects.get()
        changeBeerType = {'beerType': 'Belgian yuck'}
        res = self.client.put(
            reverse('BeerTypesDetails', kwargs={'pk': beerTypes.beerTypeId}),
            changeBeerType, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_api_delete_BeerTypes(self):
        """api can delete a beertypes."""
        self.test_api_create_BeerType()
        beerTypes = BeerTypes.objects.get()
        self.logger.debug(f"beerTypes: {beerTypes}")
        response = self.client.delete(
            reverse('BeerTypesDetails', kwargs={'pk': beerTypes.beerTypeId}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_get_BeerList(self):
        """Test the api can get a given beertypes."""
        # make sure a beer type record exists
        self.test_api_create_BeerList()
        beerList = BeerList.objects.get()
        self.logger.debug(f"beerList: {beerList}, {beerList.beerId}")
        response = self.client.get(
            reverse('BeerListDetails',
            kwargs={'pk': beerList.beerId}), format="json")
        self.logger.debug(f'response: {response.content}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, beerList)

    def test_api_update_BeerList(self):
        """Test api can update the beer list."""
        #beerTypes = self.test_api_create_BeerType()
        self.test_api_create_BeerList()
        beerList = BeerList.objects.get()
        beerTypes = BeerTypes.objects.get()
        self.logger.debug(f'the beerlist is: {beerList}, {beerList.beerId}, {beerList.beerType}')
        changeBeer = {'beerName': 'citruscity', 
                      'beerType': beerTypes.beerTypeId}
        res = self.client.put(
            reverse('BeerListDetails', kwargs={'pk': beerList.beerId}),
            changeBeer, format='json'
        )
        self.logger.debug(f"res: {res.content}")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
         
    def test_api_delete_BeerList(self):
        """can delete a beerlist."""
        self.test_api_create_BeerList()
        beerList = BeerList.objects.get()
        self.logger.debug(f"beerlist: {beerList}")
        response = self.client.delete(
            reverse('BeerListDetails', kwargs={'pk': beerList.beerId}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
