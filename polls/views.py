from django.shortcuts import render
from .forms import RezerwacjaWizyty, DodajLekarza, DodajPacjenta, SzukajLekarze, SzukajPacjenta
from .models import Lekarze, Pacjent, Wizyta
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy



class PacjentCreateView(CreateView):
    model = Pacjent
    fields = "__all__"


class WizytaCreateView(CreateView):
    model = Wizyta
    fields = "__all__"


class LekarzeCreateView(CreateView):
    model = Lekarze
    fields = "__all__"


class LekarzeUpdateView(UpdateView):
    model = Lekarze
    fields = "__all__"


class LekarzeDeleteView(DeleteView):
    model = Lekarze
    success_url = reverse_lazy('lekarze_list')


class LekarzeListView(ListView):
    model = Lekarze
    context_object_name = 'lekarze'


class WizytaListView(ListView):
    model = Wizyta
    context_object_name = 'wizyty'


class PacjentListView(ListView):
    model = Pacjent
    context_object_name = 'pacjenci'


class SzukajLekarzeFormView(FormView):
    template_name = 'polls/szukajlekarze.html'
    form_class = SzukajLekarze
    success_url = "szukajlekarze"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


class SzukajPacjentaFormView(FormView):
    template_name = 'polls/pacjent_serch.html'
    form_class = SzukajPacjenta

    def form_valid(self, form):
        return super().form_valid(form)


def index(request):
    wizyta = Wizyta.objects.all()
    return render(request, 'polls/index.html', {'wizyta': wizyta})


def wizyta_form(request):
    if request.method == "POST":
        form = RezerwacjaWizyty(request.POST)
        if form.is_valid():
            wizyta = form.save()
            return redirect('index')
    else:
        form = RezerwacjaWizyty()
    return render(request, 'polls/wizyta_form.html', {'form': form})


def lekarze_form(request):
    if request.method == "POST":
        form = DodajLekarza(request.POST)
        if form.is_valid():
            Lekarze = form.save()
            return redirect('index')
    else:
        form = DodajLekarza()
    return render(request, 'polls/lekarze_form.html', {'form': form})


def pacjent_form(request):
    if request.method == "POST":
        form = DodajPacjenta(request.POST)
        if form.is_valid():
            Pacjent = form.save()
            return redirect('index')
    else:
        form = DodajPacjenta()
    return render(request, 'polls/pacjent_form.html', {'form': form})
# dzialanie stony opisane przy pomocy klas django
# uzycie formularza dodaj pacjenta, ktorego

def lekarze_serch(request):
    lekarz_obj = None
    context = {}

    if request.method == "GET":    # pobranie danych z html
        szukane_imie = request.GET.get('fname') # przekazanie wprowadzanego tekstu z html do zmiennej z Pythona
        szukane_nazwisko = request.GET.get('lname')
# logika dzialania aplikacji na podstawie wprowadzonych danych z html
        if szukane_imie is not None and szukane_nazwisko is not None:
            if len(szukane_imie) != 0 and len(szukane_nazwisko) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    lekarz_obj = Lekarze.objects.get(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": lekarz_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    lekarz_obj = Lekarze.objects.filter(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": lekarz_obj, "wiele": len(lekarz_obj)}
        else:
                print("Nie podano imienia nai nazwiska")
    print(context)
    return render(request, 'polls/lekarze_serch.html', context=context)


def lekarze_remove(request):
    lekarz_obj = None
    context = {}

    if request.method == "GET":
        szukane_imie = request.GET.get('fname')
        szukane_nazwisko = request.GET.get('lname')

        if szukane_imie is not None and szukane_nazwisko is not None:
            if len(szukane_imie) != 0 and len(szukane_nazwisko) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    lekarz_obj = Lekarze.objects.get(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": lekarz_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    lekarz_obj = Lekarze.objects.filter(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": lekarz_obj, "wiele": len(lekarz_obj)}

    return render(request, 'polls/lekarze_remove.html', context=context)


def pacjent_serch(request):
    pacjent_obj = None
    context = {}

    if request.method == "GET":
        szukane_imie = request.GET.get('fname')
        szukane_nazwisko = request.GET.get('lname')

        if szukane_imie is not None and szukane_nazwisko is not None:
            if len(szukane_imie) != 0 and len(szukane_nazwisko) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    pacjent_obj = Pacjent.objects.get(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": pacjent_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    pacjent_obj = Pacjent.objects.filter(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": pacjent_obj, "wiele": len(pacjent_obj)}
            else:
                print("Nie podano imienia nai nazwiska")
    print(context)
    return render(request, 'polls/pacjent_serch.html', context=context)


def pacjent_remove(request):
    pacjent_obj = None
    context = {}

    if request.method == "GET":
        szukane_imie = request.GET.get('fname')
        szukane_nazwisko = request.GET.get('lname')

        if szukane_imie is not None and szukane_nazwisko is not None:
            if len(szukane_imie) != 0 and len(szukane_nazwisko) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    pacjent_obj = Pacjent.objects.get(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": pacjent_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    pacjent_obj = Pacjent.objects.filter(imie=szukane_imie, nazwisko=szukane_nazwisko)
                    context = {"object": pacjent_obj, "wiele": len(pacjent_obj)}

    return render(request, 'polls/pacjent_remove.html', context=context)


def wizyta_serch(request):
    wizyta_obj = None
    context = {}

    if request.method == "GET":
        szukane_data = request.GET.get('data_wiz')
        szukane_godzina = request.GET.get('godzina_wiz')

        if szukane_data is not None and szukane_godzina is not None:
            if len(szukane_data) != 0 and len(szukane_godzina) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    wizyta_obj = Wizyta.objects.get(wizyta_data=szukane_data, wizyta_time=szukane_godzina)
                    context = {"object": wizyta_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    wizyta_obj = Wizyta.objects.filter(wizyta_data=szukane_data, wizyta_time=szukane_godzina)
                    context = {"object": wizyta_obj, "wiele": len(wizyta_obj)}
    print(context)
    return render(request, 'polls/wizyta_serch.html', context=context)


def wizyta_remove(request):
    wizyta_obj = None
    context = {}

    if request.method == "GET":
        szukane_data = request.GET.get('data_wiz')
        szukane_godzina = request.GET.get('godzina_wiz')

        if szukane_data is not None and szukane_godzina is not None:
            if len(szukane_data) != 0 and len(szukane_godzina) != 0:
                print("Jest pytanie - szukam imienia i nazwiska")
                try:
                    wizyta_obj = Wizyta.objects.get(wizyta_data=szukane_data, wizyta_time=szukane_godzina)
                    context = {"object": wizyta_obj, "wiele": 0}
                except ObjectDoesNotExist:
                    print("ObjectDoesNotExist")
                except MultipleObjectsReturned:
                    print("MultipleObjectsReturned")
                    wizyta_obj = Wizyta.objects.filter(wizyta_data=szukane_data, wizyta_time=szukane_godzina)
                    context = {"object": wizyta_obj, "wiele": len(wizyta_obj)}
    print(context)
    return render(request, 'polls/wizyta_remove.html', context=context)


def wizyta_delete(request, wizyta_id=None):
    wizyta_to_delete = Wizyta.objects.get(id=wizyta_id)
    wizyta_to_delete.delete()
    return redirect('index')


def pacjent_delete(request, pacjent_id=None):
    pacjent_to_delete = Pacjent.objects.get(id=pacjent_id)
    pacjent_to_delete.delete()
    return redirect('index')


def lekarze_delete(request, lekarze_id=None):
    lekarze_to_delete = Lekarze.objects.get(id=lekarze_id)
    lekarze_to_delete.delete()
    return redirect('index')