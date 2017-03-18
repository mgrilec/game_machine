from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics
import json

from django.contrib.auth.models import User
from . import models

# Create your views here.
def Index(request):
    response = HttpResponse('{ "a": "b" }', content_type='text/json')
    response['last_modified'] = 'now'
    return response

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = models.UserSerializer

class LeaderboardListView(generics.ListAPIView):
    queryset = models.Leaderboard.objects.all()
    serializer_class = models.LeaderboardSerializer
    


