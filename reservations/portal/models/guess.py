from django.db import models
from datetime import datetime

class Guess(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    phone = models.CharField(max_length=20)
    is_completed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.full_name