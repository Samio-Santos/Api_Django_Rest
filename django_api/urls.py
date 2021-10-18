from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.url')),
    # path('questoes/', include('perguntas.url')),
    path('summernote/', include('django_summernote.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
