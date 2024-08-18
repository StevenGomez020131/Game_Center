from django.db import models

# Create your models here.

class contacto(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.nombre
