from django.db import models
from datetime import datetime


# Create your models here.
from ImageDrop.settings import STATIC_URL, MEDIA_URL


class User(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=15, verbose_name='Cedula', blank=False)
    photo = models.ImageField(upload_to='Foto/%Y/%M/%D', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now(), verbose_name='fecha de registro')

    def __str__(self):
        return f'Nro: {self.id} / Nombre: {self.names}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'User'
        ordering = ['id']

    def get_image(self):
        if self.photo:
            return '{}{}'.format(MEDIA_URL, self.photo)
        return '{}{}'.format(STATIC_URL, '')
