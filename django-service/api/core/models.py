from django.db import models


class User(models.model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
