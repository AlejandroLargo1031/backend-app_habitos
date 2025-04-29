from django.contrib import admin
from apps.reminder.models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'habito', 'silenciar_desde', 'silenciar_hasta', 'creado_en')
    search_fields = ('habito__nombre',)
    list_filter = ('creado_en',)