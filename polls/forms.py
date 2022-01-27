from django import forms
from .models import Pacjent, Lekarze, Wizyta


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class RezerwacjaWizyty(forms.ModelForm):

    class Meta:
        model = Wizyta
        fields = ('wizyta_data', 'wizyta_time', 'wizyta_pacjent', 'wizyta_lekarz')
        widgets = {
            'wizyta_data': DateInput(),
            'wizyta_time': TimeInput(),
        }


class DodajLekarza(forms.ModelForm):

    class Meta:
        model = Lekarze
        fields = "__all__"


class SzukajLekarze(forms.Form):
    imie = forms.CharField(max_length=30, label='Imie')
    nazwisko = forms.CharField(max_length=30, label='Nazwisko')


class DodajPacjenta(forms.ModelForm):

    class Meta:
        model = Pacjent
        fields = "__all__"


class SzukajPacjenta(forms.Form):
    RODZAJ_ZWIERZA = (
        ('Pie', 'Psy'),
        ('Kot', 'Koty'),
        ('MSa', 'Male ssaki'),
        ('DSa', 'Duze ssaki'),
        ('Gad', 'Gady'),
        ('Pta', 'Ptaki'),
        ('Inn', 'Inne'),
    )

    imie = forms.CharField(max_length=30, label='Imię')
    nazwisko = forms.CharField(max_length=30, label='Nazwisko')
    imie_zwierza = forms.CharField(max_length=30, label='Imie pacjenta')
    rodzaj_zwierza = forms.CharField(max_length=3)
