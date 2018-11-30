'''
Created on Nov. 28, 2018

@author: kjnether
'''

from django.conf.urls import include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateBeerListView
from .views import CreateBeerTypeView
from .views import UserDetailsView
from .views import UserView


urlpatterns = {
    url(r'^beertypes/$', CreateBeerTypeView.as_view(), name="CreateBeerTypeView"),
    url(r'^beerlist/$', CreateBeerListView.as_view(), name="CreateBeerListView"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
