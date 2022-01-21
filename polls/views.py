from django.shortcuts import render
from .forms import RezerwacjaWizyty, DodajLekarza, DodajPacjenta
from django.http import HttpResponse
from .models import Lekarze, Pacjent, Wizyta
from django.utils import timezone
from django.shortcuts import redirect


def index(request):
    wizyta = Wizyta.objects.all()
    return render(request, 'polls/index.html', {'wizyta': wizyta})


def wizyta_new(request):
    #wizyta = Wizyta
    if request.method == "POST":
        form = RezerwacjaWizyty(request.POST)
        if form.is_valid():
            wizyta = form.save()
          #  wizyta.wizyta_data = timezone.localdate()
          #  wizyta.wizyta_time = timezone.now()
         #   wizyta.save()
            return redirect('index')
    else:
        form = RezerwacjaWizyty()
    return render(request, 'polls/wizyta_edit.html', {'form': form})

def raporty(request):
    wizyta = Wizyta.objects.all()
    return render(request, 'polls/raporty.html', {'wizyta': wizyta})


def lekarz_new(request):
    if request.method == "POST":
        form = DodajLekarza(request.POST)
        if form.is_valid():
            Lekarze = form.save()
          #  wizyta.wizyta_data = timezone.localdate()
          #  wizyta.wizyta_time = timezone.now()
         #   wizyta.save()
            return redirect('index')
    else:
        form = DodajLekarza()
    return render(request, 'polls/lekarze_edit.html', {'form': form})


def pacjent_new(request):
    if request.method == "POST":
        form = DodajPacjenta(request.POST)
        if form.is_valid():
            Pacjent = form.save()
            #  wizyta.wizyta_data = timezone.localdate()
            #  wizyta.wizyta_time = timezone.now()
            #   wizyta.save()
            return redirect('index')
    else:
        form = DodajPacjenta()
    return render(request, 'polls/pacjent_edit.html', {'form': form})

