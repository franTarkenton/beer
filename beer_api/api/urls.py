'''
Created on Nov. 28, 2018

@author: kjnether
'''

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateBeerTypeView
from .views import CreateBeerListView

urlpatterns = {
    url(r'^beertypes/$', CreateBeerTypeView.as_view(), name="CreateBeerTypeView"),
    url(r'^beerlist/$', CreateBeerListView.as_view(), name="CreateBeerListView"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
