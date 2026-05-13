from django.db import models
from docs.models import Manual



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    ico = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ícono (clase FontAwesome)")

    def __str__(self):
        return self.name

class Resource(models.Model):
  name = models.CharField(max_length=200, verbose_name='Nombre del recurso')
  slug= models.SlugField(unique=True)
  image = models.ImageField(upload_to='resources/', blank=True, null=True)

  category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    verbose_name="Categoría",
    related_name="resources"
  )

  short_description = models.CharField(max_length=255, verbose_name='Descripción corta')
  long_description = models.TextField(verbose_name='Descripción larga')

  official_site = models.URLField(blank=True, null=True, verbose_name="Sitio Oficial")
  others_repositories = models.TextField(blank=True, null=True, verbose_name="Otros repositorios (GitHub, GitLab, etc.)")

  related_manuals = models.ForeignKey(
    Manual,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    verbose_name="Manual relacionado"
  )



  version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versión actual")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.name