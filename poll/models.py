from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
