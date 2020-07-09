from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    anfitrion = models.BooleanField(default=False)

    def __str__(self):
        """A string representation of the model."""
        return self.email