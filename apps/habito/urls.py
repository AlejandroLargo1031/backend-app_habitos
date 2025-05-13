from django.urls import path
from .views import (
    HabitoCreateView,
    HabitoListView,
    HabitoDetailView,
    HabitoUpdateView,
    HabitoDeleteView,
    ResetDailyProgressView
)


urlpatterns = [
    path('', HabitoCreateView.as_view(), name='habito-create'),  # now matches /api/habito/
    path('list/', HabitoListView.as_view(), name='habito-list'),  # now matches /api/habito/list/
    path('reset_daily_progress/', ResetDailyProgressView.as_view(), name='reset-daily-progress'),
    path('<uuid:id>/', HabitoDetailView.as_view(), name='habito-detail'),
    path('<uuid:id>/actualizar/', HabitoUpdateView.as_view(), name='habito-update'),
    path('<uuid:id>/eliminar/', HabitoDeleteView.as_view(), name='habito-delete'),
]