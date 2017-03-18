from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index),
    url(r'^user/$', views.UserListView.as_view()),
    url(r'^leaderboards/$', views.LeaderboardListView.as_view()),
]