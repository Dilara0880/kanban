from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=100)


class Column(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.DO_NOTHING)


class Task(models.Model):
    class Priority(models.TextChoices):
        easy = 'Easy'
        medium = 'Medium'
        hard = 'Hard'
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=Priority.choices, default=Priority.medium)
    column = models.ForeignKey(Column, on_delete=models.DO_NOTHING)


