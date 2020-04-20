from django.urls import path

from cyclingDB_app.view_country import CountryList, CountryDetail
from cyclingDB_app.view_cyclist import CyclistList, CyclistByTeam, CyclistDetail
from cyclingDB_app.view_race import RaceList, RaceDetail
from cyclingDB_app.view_specialty import SpecialtyList, SpecialtyDetail
from cyclingDB_app.view_stage import StageList, StageDetail
from cyclingDB_app.view_team import TeamList, TeamDetail
from cyclingDB_app.view_teamrace import TeamRaceList, TeamRaceDetail

urlpatterns = [
    path('v1/cyclist/', CyclistList.as_view(), name='Cyclist List'),
    path('v1/cyclistbyteam/<int:pk>', CyclistByTeam.as_view(), name='Cyclist by team'),
    path('v1/cyclist/<int:pk>', CyclistDetail.as_view(), name='Cyclist Detail'),

    path('v1/country/', CountryList.as_view(), name='Country List'),
    path('v1/country/<int:pk>', CountryDetail.as_view(), name='Country detail'),

    path('v1/race/', RaceList.as_view(), name='Race List'),
    path('v1/race/<int:pk>', RaceDetail.as_view(), name='Race detail'),

    path('v1/specialty/', SpecialtyList.as_view(), name='Specialty List'),
    path('v1/specialty/<int:pk>', SpecialtyDetail.as_view(), name='Specialty detail'),

    path('v1/stage/', StageList.as_view(), name='Stage List'),
    path('v1/stage/<int:pk>', StageDetail.as_view(), name='Stage detail'),

    path('v1/team/', TeamList.as_view(), name='Team List'),
    path('v1/team/<int:pk>', TeamDetail.as_view(), name='Team detail'),

    path('v1/teamrace/', TeamRaceList.as_view(), name='TeamRace List'),
    path('v1/teamrace/<int:pk>', TeamRaceDetail.as_view(), name='TeamRace detail'),
]
