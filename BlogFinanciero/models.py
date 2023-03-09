from django.db import models
    
class Post_bloguero(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    emailContacto = models.EmailField()
    tema_interes = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"
    
class Post_temas(models.Model):
    tema = models.CharField(max_length=60)
    titulo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.id} - {self.tema}"
    
class Post_lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    emailContacto = models.EmailField()
    
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"