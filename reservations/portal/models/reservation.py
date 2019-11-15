from django.db import models
from datetime import datetime
from .guess import Guess
from .table import Table

class Reservation(models.Model):
    guess = models.ForeignKey(Guess, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField()
    persons = models.IntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return "Guess: {name} - Table: {table} - Date {date}".format(name=guess.full_name, table=table.number, date=date_reservation)