import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

PAGINAS = [
    'core:inicio',
    'core:agua_y_salud',
    'core:equipos',
    'core:faq',
    'contacto:contacto',
]


class Command(BaseCommand):
    help = 'Genera el sitio estático en la carpeta dist/'

    def handle(self, *args, **options):
        base = Path(settings.BASE_DIR)
        dist = base / 'dist'
        if dist.exists():
            shutil.rmtree(dist)
        dist.mkdir()

        client = Client(HTTP_HOST='127.0.0.1')
        for nombre in PAGINAS:
            url = reverse(nombre)
            respuesta = client.get(url, secure=True)
            if respuesta.status_code != 200:
                self.stderr.write(f'ERROR {url}: {respuesta.status_code}')
                continue
            destino = dist / url.strip('/') / 'index.html'
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_bytes(respuesta.content)
            self.stdout.write(f'OK {url}')

        shutil.copytree(base / 'static', dist / 'static')
        self.stdout.write(self.style.SUCCESS('Sitio exportado en dist/'))