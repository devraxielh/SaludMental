from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Test(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    upload = models.ImageField(upload_to ='files/uploads/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="120px" />' % (self.upload.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.nombre
