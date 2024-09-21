from django.db import models


class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 100)
    published_at = models.DateField()
#   isbnn
    pages = models.PositiveIntegerField()
    languages = models.CharField(max_length= 30)
    genre = models.CharField(max_length= 50)

