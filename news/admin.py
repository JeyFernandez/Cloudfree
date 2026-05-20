from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'excerpt')
    list_filter = ('published', 'created_at')
    fieldsets = (
        ('Contenido principal', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Imagen externa', {
            'fields': ('image',),
            'description': 'Usa una URL directa a una imagen hospedada externamente.'
        }),
        ('Publicación', {
            'fields': ('author', 'published')
        }),
    )
