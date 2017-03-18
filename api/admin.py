from django.contrib import admin

from .models import leaderboard

# Register your models here.
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']

admin.site.register(leaderboard.Leaderboard, LeaderboardAdmin)
