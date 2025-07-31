# nossa_historia/urls.py

from django.urls import path
from . import views # Importa as views do app atual

urlpatterns = [
    # Quando alguém acessar a raiz do app, mostre a view 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('album/', views.nosso_album, name='nosso_album'),
    path('album/upload/', views.upload_foto, name='upload_foto'),
     path('album/delete/<int:foto_id>/', views.delete_foto, name='delete_foto'),
      path('musicas/', views.pagina_musicas, name='pagina_musicas'),
]