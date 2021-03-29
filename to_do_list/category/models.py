from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)
    description = models.TextField('Описание', null=True )
    owner = models.ForeignKey('user.User', models.CASCADE, 'category', null=True, blank=True)
    

    def __str__(self):
        return self.name



