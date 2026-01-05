"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from pymongo import MongoClient

# Simple DRF viewsets for each collection
class MongoViewSet(viewsets.ViewSet):
    collection = None
    def list(self, request):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        docs = list(db[self.collection].find())
        for doc in docs:
            doc['_id'] = str(doc['_id'])
        return Response(docs)

class UsersViewSet(MongoViewSet):
    collection = 'users'
class TeamsViewSet(MongoViewSet):
    collection = 'teams'
class ActivitiesViewSet(MongoViewSet):
    collection = 'activities'
class LeaderboardViewSet(MongoViewSet):
    collection = 'leaderboard'
class WorkoutsViewSet(MongoViewSet):
    collection = 'workouts'

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'teams', TeamsViewSet, basename='teams')
router.register(r'activities', ActivitiesViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutsViewSet, basename='workouts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
]

# API root for DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'teams': reverse('teams-list', request=request, format=format),
        'activities': reverse('activities-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workouts-list', request=request, format=format),
    })
