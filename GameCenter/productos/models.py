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
    
