from django.db import models

# Create your models here

class Autor(models.Model):
    author_id_number = models.IntegerField(default=0)
    author_user_varchar = models.CharField(max_length=200)
    author_password_varchar = models.CharField(max_length=200)
    author_pub_date_timestamp = models.DateTimeField("date published")
    author_rol_varchar = models.CharField(max_length=200)
class Articulo(models.Model):
    author_id_number = models.ForeignKey(Autor, on_delete=models.CASCADE)
    articulo_id_number = models.IntegerField(default=0)
    articulo_titulo_varchar = models.CharField(max_length=200)
    articulo_body_varchar = models.CharField(max_length=200)
    articulo_pub_date_timestamp = models.DateTimeField("date published")