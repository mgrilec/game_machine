from rest_framework import generics
from ..models import leaderboard

class LeaderboardListView(generics.ListAPIView):
    queryset = leaderboard.Leaderboard.objects.all()
    serializer_class = leaderboard.LeaderboardSerializer