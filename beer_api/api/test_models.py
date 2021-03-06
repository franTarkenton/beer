
from django.test import TestCase
from api.models.BeerTypes import BeerTypes
from api.models.BeerList import BeerList
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """Beer List Model tests."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.beerNameStr = "Red Racer"
        self.beerTypeStr = "India Pale Ale"
        self.owner = User.objects.create(username="Lebowski")
        self.beerType = BeerTypes(beerType=self.beerTypeStr, beerTypeId=1, owner=self.owner)
        self.beerList = BeerList(beerName=self.beerNameStr, beerType=self.beerType, owner=self.owner)

    def test_create_BeerType(self):
        """verify that beer we can add records to the beer list"""
        cnt1 = BeerTypes.objects.count()
        self.beerType.save()
        cnt2 = BeerTypes.objects.count()
        self.assertNotEqual(cnt1, cnt2)
        
    def test_create_BeerList(self):
        cnt1 = BeerList.objects.count()
        self.beerType.save()
        self.beerList.save()
         
        cnt2 = BeerList.objects.count()
        self.assertNotEqual(cnt1, cnt2)
        
        