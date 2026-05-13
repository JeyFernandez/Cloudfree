from django.contrib import admin
from .models import Manual, Category

# Register your models here.
admin.site.site_header = "Panel de Control CloudFree"
admin.site.site_title = "CloudFree Admin"
admin.site.index_title = "Panel"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Cambiamos 'icon' por 'ico' porque así lo nombraste en el modelo
    list_display = ('name', 'ico') 

@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    # Cambiamos 'category' por 'Category' (con C mayúscula) 
    # y 'updated_at' que también estaba en tu modelo
    list_display = ('title', 'Category', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    # Aquí también debe ir con C mayúscula
    list_filter = ('Category',)