from django.contrib import admin
from .models import Habit, DailyProgress

admin.site.register(Habit)
admin.site.register(DailyProgress)