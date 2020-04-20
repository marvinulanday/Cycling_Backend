from drf_yasg import openapi
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from cyclingDB_app.models import Race
from cyclingDB_app.serializer import RaceSerializer


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', RaceSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name', 'popularity', 'num_stages', 'country_id'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', read_only=True,
                                                               description='Race ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Race name'),
                                          'popularity': openapi.Schema(type=openapi.TYPE_NUMBER, title='Popularity'),
                                          'num_stages': openapi.Schema(type=openapi.TYPE_NUMBER, title='Num Stages'),
                                          'country': openapi.Schema(type=openapi.TYPE_NUMBER, title='Country ID'),
                                      },

                                      example={
                                          'name': 'Team name',
                                          'popularity': 100,
                                          'num_stages': 1,
                                          'country': 1,
                                      }
                                      )


class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    pagination_class = MyPagination
