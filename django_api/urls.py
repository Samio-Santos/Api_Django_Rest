from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from perguntas.api.viewsets import CespeViewSet, VunespViewSet

from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('Perguntas_Cespe', CespeViewSet, basename='Pergunta'),
router.register('Perguntas_Vunesp', VunespViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('accounts/', include('accounts.url')),
    # path('questoes/', include('perguntas.url')),
    path('summernote/', include('django_summernote.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
