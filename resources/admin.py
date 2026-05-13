from django.contrib import admin
from .models import Resource, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'ico')
    search_fields = ('name',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):    
    list_display = ('name', 'category', 'version', 'created_at') 
    
    prepopulated_fields = {'slug': ('name',)} 
    
    search_fields = ('name', 'short_description')
    
    list_filter = ('created_at', 'version', 'category')