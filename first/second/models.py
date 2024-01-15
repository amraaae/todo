from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class SubTask(models.Model):
    name = models.CharField(max_length=200)
    task = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subtasks"
    )

    def __str__(self):
        return f"{self.name}"
