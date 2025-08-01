from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # PONTO CRÍTICO: Esta é a linha que ativa o painel de administração.
    # Ela DEVE estar presente.
    path('admin/', admin.site.urls),

    # Esta linha conecta com as URLs do seu aplicativo (página inicial, album, etc.)
    path('', include('nossa_historia.urls')),

    # Esta linha serve os arquivos de mídia (fotos, músicas) em produção
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]