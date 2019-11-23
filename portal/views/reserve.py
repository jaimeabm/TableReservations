from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from ..models.guess import Guess
from ..models.reservation import Reservation
from ..models.table import Table


class Reserve(View):
    def get(self, request):
        return render(request, 'portal/reserve.html')

    def post(self, request, *args, **kwargs):
        g = None
        ctx = {'full_name': request.POST["name"],
               'email': request.POST["email"],
               'phone': request.POST["phone"],
               'persons': request.POST["persons"],
               'clockpicker': request.POST["clockpicker"],
               'date': request.POST["date"],
               'email': request.POST["email"],
               'message': request.POST["message"]}

        if Guess.objects.filter(email=ctx['email']).exists():
            g = Guess.objects.get(email=ctx['email'])
        else:
            g = Guess.objects.create(
                full_name=ctx['full_name'], email=ctx['email'], phone=ctx['phone'])

        table_count = Table.objects.filter(number_table__gte=ctx['persons']).count()

        if table_count == 0:
            messages.error(
                request, "No hay mesas disponibles para {persons}".format(persons=ctx['persons']))
            return render(request, 'portal/reserve.html', context=ctx)
        else:
            messages.success(request, "¡Su reservación se completo, gracias!")
            return redirect('reserve')

# >>> paul = Person.objects.create(name="Paul McCartney")
# >>> beatles = Group.objects.create(name="The Beatles")
# >>> m1 = Membership(person=ringo, group=beatles,
# ...     date_joined=date(1962, 8, 16),
# ...     invite_reason="Needed a new drummer.")
# >>> m1.save()

        return render(request, 'portal/reserve.html')
