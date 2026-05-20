import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from resources.models import Resource

resource = Resource.objects.filter(name='Adobe Premier Pro 2026').first()

if resource:
    print(f"Recurso actual: {resource.name}")
    print(f"Imagen actual: {resource.image if resource.image else 'Sin imagen'}")

    if resource.image:
        resource.save(update_fields=['image'])
        print(f"✓ Enlace conservado: {resource.image}")
    else:
        print("No hay enlace de imagen")
