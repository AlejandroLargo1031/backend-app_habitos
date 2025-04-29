from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyProgressViewSet

router = DefaultRouter()
router.register(r'progress', DailyProgressViewSet, basename='dailyprogress')

urlpatterns = [
    path('', include(router.urls)),
]