from rest_framework import generics

from cyclingDB_app.models import Country
from cyclingDB_app.serializer import CyclistSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CyclistSerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CyclistSerializer
