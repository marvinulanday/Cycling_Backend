from drf_yasg import openapi
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from cyclingDB_app.models import Team
from cyclingDB_app.serializer import TeamSerializer


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', TeamSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name', 'manager', 'country_id'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', read_only=True,
                                                               description='Race ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Specialty name'),
                                          'manager': openapi.Schema(type=openapi.TYPE_STRING, title='Manager name'),
                                          'country': openapi.Schema(type=openapi.TYPE_NUMBER, title='Country ID'),
                                      },

                                      example={
                                          'name': 'Team name',
                                          'manager': 'Manager name',
                                          'country': 1
                                      }
                                      )


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = MyPagination
