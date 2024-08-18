from django.db import models

# Create your models here.

class comentarios(models.Model): #Define la estructura de nuestra tabla
    nombre = models.TextField()#Texto largo
    descripcion = models.TextField()#Texto largo
    crated = models.DateField(auto_now_add=True,verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Actualizado")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comenarios"
        ordering = ["-crated"]
        #El menos indica que se ordenara del más reciente al más viejo
    
    def _str_(self):
        return self.nombre
        #Indica que se mostrará el nombre como el valor en la tabla