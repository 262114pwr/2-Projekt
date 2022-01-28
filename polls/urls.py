"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic import DeleteView
from polls.views import LekarzeListView, WizytaListView, PacjentListView


urlpatterns = [
    path('', views.index, name='index'),
    path('wizyta_list', WizytaListView.as_view(), name='wizyta_list'),
    path('lekarze_form', views.lekarze_form, name='lekarze_form'),
    path('pacjent_form', views.pacjent_form, name='pacjent_form'),
    path('wizyta_form', views.wizyta_form, name='wizyta_form'),
    path('pacjent_list', PacjentListView.as_view(), name='pacjent_list'),
    path('lekarze_serch', views.lekarze_serch, name='lekarze_serch'),
    path('lekarze_remove', views.lekarze_remove, name='lekarze_remove'),
    path('pacjent_serch', views.pacjent_serch, name='pacjent_serch'),
    path('pacjent_remove', views.pacjent_remove, name='pacjent_remove'),
    path('wizyta_serch', views.wizyta_serch, name='wizyta_serch'),
    path('wizyta_remove', views.wizyta_remove, name='wizyta_remove'),
    path('lekarze_list', LekarzeListView.as_view(), name='lekarze_list'),
    path('wizyta_delete/<wizyta_id>', views.wizyta_delete, name='wizyta_delete'),
    # wizyta_id zwraca strona
    path('pacjent_delete/<pacjent_id>', views.pacjent_delete, name='pacjent_delete'),
    path('lekarze_delete/<lekarze_id>', views.lekarze_delete, name='lekarze_delete'),
]
# laczymy kod z Pythona z views z stronami html
# kod views opisuje dzialanie strony a kod html opisuje wyglad strony
# pacjent list lkasa
# list jako klasa
