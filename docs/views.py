import markdown
from django.shortcuts import render, get_object_or_404
from .models import Manual, Category
from news.models import News
from resources.models import Resource

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

    # 5 noticias más recientes
    noticias_recientes = News.objects.filter(published=True).order_by('-created_at')[:5]

    # Recursos nuevos para la barra lateral
    recursos_nuevos = Resource.objects.all().order_by('-created_at')[:4]

    context = {
        'manuales_recientes': manuales_recientes,
        'noticias_recientes': noticias_recientes,
        'recursos_nuevos': recursos_nuevos,
        'site_name': 'CloudFree'
    }
    return render(request, 'home.html', context)

def all_manuals(request):
    # EL CAMBIO: .all() va primero, luego el prefetch
    categories = Category.objects.all().prefetch_related('manual_set')
    
    return render(request, 'docs/all_manuals.html', {
        'categories': categories,
    })