from django.db import models
from datetime import datetime

class Table(models.Model):
    number_table = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return "Table: {number} - size: {size}".format(number=self.number_table, size=self.size)