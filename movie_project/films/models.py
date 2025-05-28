from django.db import models

class Movie(models.Model):
    title = models.CharField('Название',max_length=50)
    description = models.TextField('Описание')
    feedback = models.TextField('Отзыв',null=True,blank=True)