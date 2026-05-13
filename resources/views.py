# resources/views.py
from django.shortcuts import render, get_object_or_404
from .models import Resource, Category

def resource_list(request):
    categories = Category.objects.all().prefetch_related('resources')
    return render(request, 'resources/resource_list.html', {'categories': categories})

def resource_detail(request, slug):
    resource = get_object_or_404(Resource, slug=slug)
    return render(request, 'resources/resource_detail.html', {'resource': resource})