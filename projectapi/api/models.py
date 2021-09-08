from django.db import models
from django.db.models.fields import CharField

class Person(models.Model):
    name =models.CharField(max_length=30 )
    email =models.EmailField(max_length=50)
    about = models.TextField(max_length=300)

    def __str__(self):
        return  self.name
