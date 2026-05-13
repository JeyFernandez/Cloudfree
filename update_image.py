import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from resources.models import Resource

# Ver qué imágenes hay disponibles
media_resources_path = 'media/resources'
if os.path.exists(media_resources_path):
    files = os.listdir(media_resources_path)
    print("Archivos en media/resources:")
    for f in files:
        print(f"  - {f}")
    print()

# Actualizar el recurso para usar el PNG si existe
resource = Resource.objects.filter(name='Adobe Premier Pro 2026').first()

if resource:
    print(f"Recurso actual: {resource.name}")
    print(f"Imagen actual: {resource.image.name if resource.image else 'Sin imagen'}")
    
    # Buscar archivo PNG o imagen disponible
    png_file = 'Logo-Premiere-Pro.png'
    svg_file = 'Logo-Premiere-Pro.svg'
    
    if os.path.exists(os.path.join(media_resources_path, png_file)):
        resource.image.name = f'resources/{png_file}'
        resource.save()
        print(f"✓ Actualizado a: {resource.image.name}")
    elif os.path.exists(os.path.join(media_resources_path, svg_file)):
        resource.image.name = f'resources/{svg_file}'
        resource.save()
        print(f"✓ Actualizado a: {resource.image.name}")
    else:
        print("No se encontró imagen")
