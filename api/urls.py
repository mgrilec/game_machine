from django.conf.urls import url

from .views import leaderboard

urlpatterns = [
    # url(r'^$', views.Index),
    # url(r'^user/$', views.UserListView.as_view()),
    url(r'^leaderboards/$', leaderboard.LeaderboardListView.as_view()),
]