from django.db import models

# Create your models here.

class accesoriosXbox(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Accesorio Xbox"
        verbose_name_plural = "Accesorios Xbox"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.nombre

class imagenesProductos(models.Model):
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.descripcion


    
