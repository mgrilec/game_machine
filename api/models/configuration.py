from django.db import models
from django.conf import settings
from rest_framework import serializers

class Configuration(models.Model):
    name = models.CharField(default="default")
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL)
    created_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('id', 'created_by', 'name', 'entries', 'created_at', 'deleted_at')
    
class ConfigurationEntry(models.Model):
    key = models.CharField(max_length = 1024)
    value = models.TextField()
    configuration = models.OneToOneField(Configuration, related_name="entries")
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL)
    created_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

class ConfigurationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationEntry
        fields = ('id', 'key', 'value', 'configuration', 'created_by', 'created_at', 'deleted_at')
