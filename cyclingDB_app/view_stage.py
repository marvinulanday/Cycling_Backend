from drf_yasg import openapi
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from cyclingDB_app.models import Stage
from cyclingDB_app.serializer import StageSerializer


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class StageList(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    pagination_class = MyPagination


category_response = openapi.Response('Response description', StageSerializer)

request_category_put = openapi.Schema(type=openapi.TYPE_OBJECT,
                                      required=['name', 'day', 'month', 'stage_number', 'stage_km', 'race_id',
                                                'specialty_id'],
                                      properties={
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER, title='ID', read_only=True,
                                                               description='Stage ID'),
                                          'name': openapi.Schema(type=openapi.TYPE_STRING, title='Stage name'),
                                          'day': openapi.Schema(type=openapi.TYPE_NUMBER, title='Stage day'),
                                          'month': openapi.Schema(type=openapi.TYPE_NUMBER, title='Stage month'),
                                          'stage_number': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                                         title='Stage numbers'),
                                          'stage_km': openapi.Schema(type=openapi.TYPE_NUMBER, title='Stage Kms'),
                                          'race': openapi.Schema(type=openapi.TYPE_NUMBER, title='Race ID'),
                                          'specialty': openapi.Schema(type=openapi.TYPE_NUMBER, title='Specialty ID'),
                                      },

                                      example={
                                          'name': 'Stage name',
                                          'day': 1,
                                          'month': 1,
                                          'stage_number': 1,
                                          'stage_km': 1,
                                          'race': 1,
                                          'specialty': 1
                                      }
                                      )


class StageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    pagination_class = MyPagination
