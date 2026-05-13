import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from resources.models import Resource

# Ver los recursos y sus imágenes
for resource in Resource.objects.all():
    print(f'Recurso: {resource.name}')
    if resource.image:
        print(f'  Image: {resource.image.name}')
        print(f'  Image URL: {resource.image.url}')
    else:
        print(f'  Sin imagen')
    print()
