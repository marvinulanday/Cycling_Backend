from drf_yasg import openapi
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from cyclingDB_app.models import TeamRace
from cyclingDB_app.serializer import TeamRaceSerializer


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class TeamRaceList(generics.ListCreateAPIView):
    queryset = TeamRace.objects.all()
    serializer_class = TeamRaceSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', TeamRaceSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['race_id', 'team_id'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', read_only=True,
                                                               description='TeamRace ID'),
                                          'race': openapi.Schema(type=openapi.TYPE_NUMBER, title='Race ID'),
                                          'team': openapi.Schema(type=openapi.TYPE_NUMBER, title='Team ID'),
                                      },

                                      example={
                                          'race': 1,
                                          'team': 1
                                      }
                                      )


class TeamRaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamRace.objects.all()
    serializer_class = TeamRaceSerializer
    pagination_class = MyPagination
