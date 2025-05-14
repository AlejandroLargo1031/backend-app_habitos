from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HydrationViewSet, HydrationReminderViewSet

router = DefaultRouter()
router.register(r'records', HydrationViewSet, basename='hydration-records')
router.register(r'reminders', HydrationReminderViewSet, basename='hydration-reminders')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', HydrationViewSet.as_view({'get': 'dashboard'}), name='hydration-dashboard'),
    path('add_glass/', HydrationViewSet.as_view({'post': 'add_glass'}), name='hydration-add-glass')
]