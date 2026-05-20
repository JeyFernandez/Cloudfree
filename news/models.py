from django.db import models
from django.contrib.auth import get_user_model


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name='Imagen (URL)',
        help_text='Pega aquí un enlace directo a la imagen alojada externamente.'
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
