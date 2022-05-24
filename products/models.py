from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):
    main_img = models.ImageField(upload_to='images/')
    img_1 = models.ImageField(upload_to='images/',blank=True)
    img_2 = models.ImageField(upload_to='images/',blank=True)
    img_3 = models.ImageField(upload_to='images/',blank=True)
    alt_text = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = RichTextField()

    def __str__(self):
        return self.title