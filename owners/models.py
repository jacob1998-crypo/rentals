from django.db import models
from datetime import datetime


class Owners(models.Model):
    name = models.CharField(max_length=200)
    ID_number = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='default_photo.jpg')
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
