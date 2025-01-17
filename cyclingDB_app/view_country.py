from drf_yasg import openapi
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from cyclingDB_app.models import Country
from cyclingDB_app.serializer import CountrySerializer


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', CountrySerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', read_only=True,
                                                               description='Country ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Country name'),
                                      },

                                      example={
                                          'name': 'Country name'
                                      }
                                      )


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = MyPagination
