from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.TextChoices(['Easy', 'Medium', 'Hard'])


class Column(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2050)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Board(models.Model):
    title = models.CharField(max_length=100)
    columns = models.ForeignKey(Column, on_delete=models.CASCADE)