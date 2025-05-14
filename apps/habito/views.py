from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Habito
from .serializers import HabitoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from datetime import date, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
 

class HabitoViewSet(viewsets.ModelViewSet):
    queryset = Habito.objects.all()
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)  

class HabitoListView(generics.ListAPIView):
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)
    
class HabitoDetailView(generics.RetrieveAPIView):
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)
    
class HabitoUpdateView(generics.UpdateAPIView):
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    http_method_names = ['patch']  

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.save(partial=True) 
        
    def perform_update(self, serializer):
        instance = self.get_object()
        allowed_fields = {
            'nombre', 'objetivo', 'actual', 'frecuencia',
            'meta_unidad', 'tipo_habito', 'racha_actual',
            'racha_record', 'completed_dates', 'icono', 'color'
        }
        
        update_data = {
            k: v for k, v in serializer.validated_data.items() 
            if k in allowed_fields
        }
        
        # Actualizar campos
        for attr, value in update_data.items():
            setattr(instance, attr, value)
        
        # Actualizar rachas
        if 'completed_dates' in update_data:
            instance.update_streaks()
        
        instance.save()

class HabitoDeleteView(generics.DestroyAPIView):
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)

class HabitoCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            data = request.data.copy()
            data["tipo_habito"] = "cuantitativo"
            data["color"] = "#34D399"

            serializer = HabitoSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(usuario=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class ResetDailyProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today = date.today()
        habits = Habito.objects.filter(usuario=request.user)
        
        for habit in habits:
            if habit.last_reset != today:
                habit.actual = 0
                habit.last_reset = today

                yesterday = today - timedelta(days=1)

                if not habit.completed_dates.filter(fecha=yesterday).exists():
                    habit.racha_actual = 0

                habit.save()
        
        return Response({'status': 'daily progress reset'})

