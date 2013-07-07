from django.db import models

class Raw(models.Model):
    data = models.TextField()
