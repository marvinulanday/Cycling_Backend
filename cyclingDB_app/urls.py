from django.urls import path

from cyclingDB_app.view_country import CountryList, CountryDetail
from cyclingDB_app.view_cyclist import CyclistList, CyclistByTeam

urlpatterns = [
    path('v1/cyclist/', CyclistList.as_view(), name='Cyclist List'),
    path('v1/cyclistbyteam/<int:pk>', CyclistByTeam.as_view(), name='Cyclist by team'),
    path('v1/cyclist/<int:pk>', CyclistByTeam.as_view(), name='Cyclist by team'),
    path('v1/country/', CountryList.as_view(), name='Country List'),
    path('v1/country/<int:pk>', CountryDetail.as_view(), name='Country detail'),
]
