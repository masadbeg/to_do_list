from django.db import models

class Task(models.Model):
    title = models.CharField ('Заголовок', max_length=255)
    description = models.TextField ('Описание')
    deadline = models.DateTimeField('Дата и время выполнения', auto_now_add=True)
    category = models.ForeignKey ('category.Category', models.CASCADE, 'task')
    owner = models.ForeignKey('user.User', models.CASCADE, 'task')
    
    # def __str__(self):
    #     return sel