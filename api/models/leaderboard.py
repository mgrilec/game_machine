from django.db import models
from django.conf import settings
from rest_framework import serializers

from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'username')

class Game(models.Model):
    pass

# leaderboard
class Leaderboard(models.Model):
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(blank=False, null=False, max_length=80)
    description = models.CharField(max_length=1024)
    created_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ('id', 'created_by', 'name', 'description', 'created_at', 'deleted_at')

# entry in an leaderboard
class LeaderboardEntry(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    score = models.FloatField()
    leaderboard = models.OneToOneField(Leaderboard, related_name='entries')
    created_at = models.DateField(auto_now=True)
    deleted_at = models.DateField()
    