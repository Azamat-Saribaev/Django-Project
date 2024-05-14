from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    year = models.DateField()
    price = models.IntegerField()
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.title
