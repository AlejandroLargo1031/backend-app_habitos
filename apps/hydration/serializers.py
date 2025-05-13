# apps/hydration/serializers.py
from rest_framework import serializers
from .models import HydrationRecord, HydrationReminder, HydrationStats
from django.contrib.auth import get_user_model
from datetime import date, timedelta

User = get_user_model()

class HydrationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydrationRecord
        fields = ['id', 'date', 'amount', 'goal']
        read_only_fields = ['id', 'date']

class HydrationReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydrationReminder
        fields = ['id', 'time', 'is_active']
        read_only_fields = ['id']

class HydrationStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydrationStats
        fields = ['current_streak', 'longest_streak']
        read_only_fields = fields

class UserHydrationSerializer(serializers.ModelSerializer):
    today_record = serializers.SerializerMethodField()
    weekly_records = serializers.SerializerMethodField()
    hydration_reminders = HydrationReminderSerializer(many=True, read_only=True)
    hydration_stats = HydrationStatsSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['today_record', 'weekly_records', 'hydration_reminders', 'hydration_stats']

    def get_today_record(self, obj):
        record = obj.hydration_records.filter(date=date.today()).first()
        return HydrationRecordSerializer(record).data if record else {'amount': 0, 'goal': 8}

    def get_weekly_records(self, obj):
        week_ago = date.today() - timedelta(days=6)
        records = obj.hydration_records.filter(date__gte=week_ago).order_by('date')
        return HydrationRecordSerializer(records, many=True).data