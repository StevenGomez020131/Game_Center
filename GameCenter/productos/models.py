from django.db import models
from django.conf import settings
# Create your models here.

class accesoriosXbox(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
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
    
class JuegosXbox(models.Model):
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Juego Xbox"
        verbose_name_plural = "Juegos Xbox"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.nombre

class accesoriosPlayStation(models.Model):
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Accesorio PlayStation"
        verbose_name_plural = "Accesorios PlayStation"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.nombre
    

class accesoriosNintendo(models.Model):
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Accesorio Nintendo"
        verbose_name_plural = "Accesorios Nintendo"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.nombre

class accesoriosPC(models.Model):
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Accesorio PC"
        verbose_name_plural = "Accesorios PC"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.nombre







    
