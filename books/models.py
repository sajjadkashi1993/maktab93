from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    status = models.ManyToManyField(max_length=250)


    class Meta:
        ordering=['name']


    def __str__(self):
        return f'{self.id}'


