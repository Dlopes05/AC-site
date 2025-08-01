import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    """
    Comando para criar um superusuário de forma não-interativa,
    mas que não falha se o usuário já existir.
    """
    help = "Cria um superusuário usando variáveis de ambiente, sem falhar se ele já existir."

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not all([username, email, password]):
            self.stdout.write(self.style.ERROR(
                "As variáveis de ambiente DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD devem ser definidas."
            ))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f"Criando conta para o superusuário: {username}"))
            User.objects.create_superuser(email=email, username=username, password=password)
        else:
            self.stdout.write(self.style.WARNING(f"Superusuário '{username}' já existe. Nenhuma ação foi tomada."))