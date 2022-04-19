from django.db import models
from django.shortcuts import reverse

# Create your models here.
# class News(models.Model):
# 	title = models.CharField(max_length=250, db_index=True)
# 	slug = models.SlugField(max_length=250, unique=True)
# 	body = models.TextField(blank=True)
# 	date = models.DateField(auto_now_add=True)

# 	def __str__(self):
# 		return self.title

	#def get_absolute_url(self):
		#return reverse('news_page_url', kwargs={'slug': self.slug})
  
  
class Catalogo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to="cortes", null=True)
    
    def __str__(self):
        return self.nombre