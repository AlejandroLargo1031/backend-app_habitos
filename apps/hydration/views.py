# apps/hydration/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response  # ¡Este es el import correcto!
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from datetime import date, timedelta
from .models import HydrationRecord, HydrationReminder, HydrationStats
from .serializers import HydrationReminderSerializer, UserHydrationSerializer

User = get_user_model()

class HydrationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def initialize_streak(self, user):
        """Inicializa las estadísticas de racha si no existen"""
        stats, created = HydrationStats.objects.get_or_create(user=user)
        return stats

    def update_streak(self, user):
        """Actualiza las estadísticas de racha del usuario"""
        stats = self.initialize_streak(user)
        today = date.today()
        yesterday = today - timedelta(days=1)

        try:
            yesterday_record = HydrationRecord.objects.get(user=user, date=yesterday)
            stats.current_streak = stats.current_streak + 1 if yesterday_record.amount >= yesterday_record.goal else 0
        except HydrationRecord.DoesNotExist:
            stats.current_streak = 0

        if stats.current_streak > stats.longest_streak:
            stats.longest_streak = stats.current_streak

        stats.save()
        return stats

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        """Endpoint para el dashboard de hidratación"""
        user = request.user
        self.update_streak(user)
        
        serializer = UserHydrationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_glass(self, request):
        user = request.user
        today = date.today()

        # Obtener o crear el registro de hoy
        record, created = HydrationRecord.objects.get_or_create(user=user, date=today)

        # Incrementar la cantidad de agua
        record.amount += 1
        record.save()

        return Response({'message': 'Vaso añadido', 'amount': record.amount}, status=status.HTTP_200_OK)

class HydrationReminderViewSet(viewsets.ModelViewSet):
    serializer_class = HydrationReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HydrationReminder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)