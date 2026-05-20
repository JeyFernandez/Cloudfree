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
  image = models.URLField(
    blank=True,
    null=True,
    verbose_name='Imagen (URL)',
    help_text='Pega un enlace directo a la imagen alojada fuera del proyecto.'
  )

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
  others_repositories = models.TextField(
    blank=True,
    null=True,
    verbose_name="Enlaces de descarga",
    help_text="Un enlace por línea. Formatos válidos: https://... | Etiqueta | Fuente"
  )

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

  def get_download_links(self):
    links = []

    if not self.others_repositories:
      return links

    for raw_line in self.others_repositories.splitlines():
      line = raw_line.strip()
      if not line:
        continue

      label = 'Descargar'
      source = ''
      url = line

      parts = [part.strip() for part in line.split('|')]

      if len(parts) == 2:
        first, second = parts
        if second.startswith('http://') or second.startswith('https://'):
          label = first or 'Descargar'
          url = second
        elif first.startswith('http://') or first.startswith('https://'):
          label = second or 'Descargar'
          url = first
      elif len(parts) >= 3:
        first, second, third = parts[0], parts[1], parts[2]
        if first.startswith('http://') or first.startswith('https://'):
          url = first
          label = second or 'Descargar'
          source = third
        elif second.startswith('http://') or second.startswith('https://'):
          label = first or 'Descargar'
          url = second
          source = third

      links.append({
        'label': label,
        'url': url,
        'source': source,
      })

    return links