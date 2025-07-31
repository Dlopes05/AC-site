# nossa_historia/views.py

# A CORREÇÃO ESTÁ AQUI: Adicionamos get_object_or_404 à lista de importações
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Foto,Musica

# ---------------------------------
# View da Página Inicial
def pagina_inicial(request):
    return render(request, 'nossa_historia/pagina_inicial.html')

# ---------------------------------
# View do Álbum
def nosso_album(request):
    fotos = Foto.objects.all().order_by('-data_adicionada')
    return render(request, 'nossa_historia/nosso_album.html', {'fotos': fotos})

# ---------------------------------
# View de Upload de Foto
def upload_foto(request):
    if request.method == 'POST':
        nova_foto_arquivo = request.FILES.get('imagem')
        if nova_foto_arquivo:
            foto = Foto.objects.create(imagem=nova_foto_arquivo)
            return JsonResponse({'status': 'ok', 'url': foto.imagem.url, 'id': foto.id})
    return JsonResponse({'status': 'error', 'message': 'Requisição inválida.'})

# ---------------------------------
# View de Exclusão de Foto
def delete_foto(request, foto_id):
    if request.method == 'POST':
        # Agora o Django saberá o que esta função faz
        foto = get_object_or_404(Foto, id=foto_id)
        foto.delete()
        return JsonResponse({'status': 'ok', 'message': 'Foto excluída com sucesso.'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)

def pagina_musicas(request):
    # Busca todos os objetos Musica no banco de dados
    # A ordenação já foi definida no models.py (class Meta)
    musicas = Musica.objects.all()
    # Envia a lista de músicas para o template
    return render(request, 'nossa_historia/pagina_musicas.html', {'musicas': musicas})