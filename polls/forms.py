from django import forms
from .models import Pacjent, Lekarze, Wizyta


class RezerwacjaWizyty(forms.ModelForm):

    class Meta:
        model = Wizyta
        fields = "__all__"


class DodajLekarza(forms.ModelForm):

    class Meta:
        model = Lekarze
        fields = "__all__"


class DodajPacjenta(forms.ModelForm):

    class Meta:
        model = Pacjent
        fields = "__all__"
