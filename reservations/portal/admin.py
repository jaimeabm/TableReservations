from django.contrib import admin
from .models.guess import Guess
from .models.reservation import Reservation
from .models.table import Table

# Register your models here.
admin.site.register(Guess)
admin.site.register(Reservation)
admin.site.register(Table)