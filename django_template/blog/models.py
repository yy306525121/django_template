from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=500)
    class Meta:
        app_label = 'blog'