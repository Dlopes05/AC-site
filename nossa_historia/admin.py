# nossa_historia/admin.py
from django.contrib import admin
from .models import Foto, Musica # Importe o seu modelo Foto

# Registre o modelo
admin.site.register(Foto)
admin.site.register(Musica)