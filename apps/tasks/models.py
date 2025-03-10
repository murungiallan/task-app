from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_At = models.DateField(auto_now_add=True)
    updated_At = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
