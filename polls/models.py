from django.db import models
from django.urls import reverse


class Lekarze(models.Model):
    SPEC_NAUK = (
        ('Chi', 'Chirurg'),
        ('Ort', 'Ortopeda'),
        ('Ogl', 'Ogolne'),
        ('Kar', 'Kardiolog'),
    )
    SPEC_LECZ = (
        ('Pie', 'Psy'),
        ('Kot', 'Koty'),
        ('MSa', 'Male ssaki'),
        ('DSa', 'Duze ssaki'),
        ('Gad', 'Gady'),
        ('Pta', 'Ptaki'),
    )
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    tytul_nauk = models.CharField(max_length=30)
    specjalizacja_naukowa = models.CharField(max_length=3, choices=SPEC_NAUK)
    specjalizacja_leczenia = models.CharField(max_length=3, choices=SPEC_LECZ)
    opis_text = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return "{0.tytul_nauk}, {0.imie},{0.nazwisko}, {0.specjalizacja_naukowa}, " \
               "{0.specjalizacja_leczenia}".format(self)

    class Meta:
        verbose_name = "Lekarz"
        verbose_name_plural = "Lekarze"
        ordering = ['nazwisko']

    def get_absolute_url(self):
        return reverse('lekarze_new', kwargs={'pk': self.pk})


class Pacjent(models.Model):
    RODZAJ_ZWIERZA = (
        ('Pie', 'Psy'),
        ('Kot', 'Koty'),
        ('MSa', 'Male ssaki'),
        ('DSa', 'Duze ssaki'),
        ('Gad', 'Gady'),
        ('Pta', 'Ptaki'),
        ('Inn', 'Inne'),
    )
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    imie_zwierza = models.CharField(max_length=30)
    rodzaj_zwierza = models.CharField(max_length=3, choices=RODZAJ_ZWIERZA)
    phone_number = models.CharField(max_length=12, verbose_name='Numer telefonu')
    address = models.CharField(max_length=256, verbose_name='Adres')
    description = models.CharField(max_length=516, verbose_name='Powod wizyty')
    email_address = models.EmailField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return "{0.imie}, {0.nazwisko} ".format(self)

    class Meta:
        verbose_name = "Pacjent"
        verbose_name_plural = "Pacjenci"
        ordering = ['nazwisko']

    def get_absolute_url(self):
        return reverse('pacjent_new', kwargs={'pk': self.pk})


class Wizyta(models.Model):
    wizyta_data = models.DateField(blank=True, null=True, verbose_name='Data wizyty')
    wizyta_time = models.TimeField(blank=True, null=True, verbose_name='Godzina wizyty')
    wizyta_pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE, verbose_name='Pacjent')
    wizyta_lekarz = models.ForeignKey(Lekarze, on_delete=models.CASCADE, verbose_name='Lekarz')
    objects = models.Manager()

    def __str__(self):
        return "{0.wizyta_data}, {0.wizyta_time}, {0.wizyta_pacjent}, {0.wizyta_lekarz} ".format(self)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"
        ordering = ['wizyta_data']

    def get_absolute_url(self):
        return reverse('wizyta_new', kwargs={'pk': self.pk})
