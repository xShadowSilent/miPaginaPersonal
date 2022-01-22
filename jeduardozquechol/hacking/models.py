from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Hacking(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="hacking")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "hacking"
        verbose_name_plural = "hackings"
        ordering = ['-created']

    def __str__(self):
        return self.title