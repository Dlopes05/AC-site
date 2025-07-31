# nossa_historia/models.py
from django.db import models
from django.utils import timezone

class Foto(models.Model):
    # O campo para guardar o arquivo da imagem
    imagem = models.ImageField(upload_to='album_fotos/')
    # Um campo opcional para uma legenda
    legenda = models.CharField(max_length=100, blank=True, null=True)
    data_foto = models.DateField(default=timezone.now, help_text="A data em que a foto foi tirada.")
    # A data em que a foto foi adicionada, preenchida automaticamente
    data_adicionada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto adicionada em {self.data_adicionada.strftime('%d/%m/%Y')}"
    
class Musica(models.Model):
    # --- Informações da Música ---
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    duracao = models.CharField(max_length=10, help_text="Formato: MM:SS", blank=True)
    letra = models.TextField(blank=True) # blank=True significa que o campo é opcional

    # --- Arquivos de Mídia ---
    # Para a capa do álbum/single
    capa = models.ImageField(upload_to='capas_musicas/', help_text="Capa do álbum ou single")

    # --- Fontes da Música (pelo menos uma deve ser preenchida) ---
    # Para o upload de um arquivo MP3
    arquivo_mp3 = models.FileField(upload_to='musicas_mp3/', blank=True, null=True, help_text="Faça upload de um arquivo MP3")
    
    # Para o link do YouTube
    link_youtube = models.URLField(blank=True, null=True, help_text="Cole o link do YouTube aqui")

    data_adicionada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

    class Meta:
        # Ordena as músicas pela data em que foram adicionadas, as mais novas primeiro
        ordering = ['-data_adicionada']