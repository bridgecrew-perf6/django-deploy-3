from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Hero(models.Model):
    img = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title