

from django.contrib import admin

from .models import Lekarze, Pacjent, Wizyta

admin.site.register(Lekarze)
admin.site.register(Pacjent)
admin.site.register(Wizyta)
