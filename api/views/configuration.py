from rest_framework import generics
from ..models import configuration

class ConfigurationListView(generics.ListAPIView):
    queryset = configuration.Configuration.objects.all()
    serializer_class = configuration.ConfigurationSerializer