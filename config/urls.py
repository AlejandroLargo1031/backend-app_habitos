from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from apps.auth.views import clerk_webhook


schema_view = get_schema_view(
    openapi.Info(
        title="Hábitos API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/auth/', include('apps.users.urls')),
    path('api/habito/', include('apps.habito.urls')),
    path('api/hydration/', include('apps.hydration.urls')),  # Incluye las rutas de hydration
    path('api/progress/', include('apps.dailyProgress.urls')),  # Incluye las rutas de dailyProgress
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/auth/webhook/', clerk_webhook),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]