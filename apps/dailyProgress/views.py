from rest_framework import viewsets, permissions
from apps.dailyProgress.models import DailyProgress
from apps.dailyProgress.serializers import DailyProgressSerializer

class DailyProgressViewSet(viewsets.ModelViewSet):
    serializer_class = DailyProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DailyProgress.objects.filter(habito__usuario=self.request.user)