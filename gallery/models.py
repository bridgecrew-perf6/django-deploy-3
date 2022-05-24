from django.db import models

# Create your models here.


class Gallery(models.Model) :
    img = models.ImageField(upload_to='images/')
    alt_text = models.TextField(max_length = 50)

    def __str__(self):
        return str(self.id)