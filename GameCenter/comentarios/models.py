from django.db import models

# Create your models here.

class comentarios(models.Model): #Define la estructura de nuestra tabla
    nombre = models.TextField()#Texto largo
    descripcion = models.TextField()#Texto largo
    created = models.DateField(auto_now_add=True,verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Actualizado")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comenarios"
        ordering = ["-created"]
        #El menos indica que se ordenara del más reciente al más viejo
    
    def _str_(self):
        return self.nombre
        #Indica que se mostrará el nombre como el valor en la tabla

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje
#Indica que se mostrára el mensaje como valor en la tabla