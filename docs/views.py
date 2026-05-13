import markdown
from django.shortcuts import render, get_object_or_404
from .models import Manual, Category

def manual_detail(request, slug):
    manual = get_object_or_404(Manual, slug=slug)
    
    # Convertimos el texto a HTML con soporte para bloques de código
    manual.content = markdown.markdown(manual.content, extensions=['fenced_code', 'codehilite'])
    # Traer otros manuales de la misma categoría para el índice lateral
    related_manuales = Manual.objects.filter(Category=manual.Category).order_by('-created_at')

    context = {
        'manual': manual,
        'related_manuales': related_manuales,
    }

    return render(request, 'docs/manual_detail.html', context)



def home(request):
    # Obtenemos los 5 manuales más recientes de la base de datos
    manuales_recientes = Manual.objects.all().order_by('-created_at')[:5]
    
    # Lista de módulos para la barra lateral derecha
    modules = [
        {'name': 'Documentación', 'url': '/manuales/'},
        {'name': 'Registro', 'url': '/accounts/registro/'},
        {'name': 'Admin', 'url': '/admin/'},
    ]

    context = {
        'manuales_recientes': manuales_recientes,
        'modules': modules,
        'site_name': 'CloudFree'
    }
    return render(request, 'home.html', context)

def all_manuals(request):
    # EL CAMBIO: .all() va primero, luego el prefetch
    categories = Category.objects.all().prefetch_related('manual_set')
    
    return render(request, 'docs/all_manuals.html', {
        'categories': categories,
    })