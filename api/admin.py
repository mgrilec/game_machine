from django.contrib import admin

from . import models

# Register your models here.
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']

admin.site.register(models.Leaderboard, LeaderboardAdmin)
