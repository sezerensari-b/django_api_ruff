from django.db import models
from django.core.validators import MaxValueValidator


class BookSubject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=180, unique=True)
    author = models.CharField(max_length=100)
    page = models.PositiveIntegerField(validators=[MaxValueValidator(250)])
    subject = models.ForeignKey(BookSubject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
