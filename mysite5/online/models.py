from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    """docstring forUser  """
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self, arg):
        return self.username
