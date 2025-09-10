from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from .models import Uzytkownicy
from .forms import DodajPrzepis
from .models import Przepisy
# Create your views here.

# crud - create retrieve update delete

def dodaj_przepis(request):
    if request.method == 'POST':
        form = DodajPrzepis(request.POST)
        if(form.is_valid()):
            nazwa = form.cleaned_data['NazwaDania']
            autor = form.cleaned_data['AutorPrzepisu']
            rodzaj = form.cleaned_data['RodzajKuchni']
            produktyy = form.cleaned_data['Produkty']
            przepisd = form.cleaned_data['PrzepisDania']
            przepis = Przepisy(NazwaDania = nazwa, AutorPrzepisu = autor, RodzajKuchni = rodzaj, Produkty = produktyy,  PrzepisDania = przepisd)
            przepis.save()
            return HttpResponse("Success")
        else:
            return HttpResponseBadRequest("Failed")
    else:
        form = DodajPrzepis()
        return render(request, 'dodaj.html', {'form': form})



def index(request):
    return render(request, 'index.html',
    {

    })

def mieso(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "mieso.html", context)

def weganskie(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "weganskie.html", context)

def wegetarianskie(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "wegetarianskie.html", context)

def jarskie(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "jarskie.html", context)

def bezglutenowe(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "bezglutenowe.html", context)

def lista(request):
    lista_przepisow = Przepisy.objects.all()
    context ={

        'lista_przepisow': lista_przepisow
    }
    return render(request, "lista.html", context)

def uzytkownicy(request):
    user_objects = Uzytkownicy.objects.all()
    context = {
        'user_objects': user_objects
    }
    return render(request, "uzytkownicy.html", context) 

def szukaj(request):
    return render(request, 'szukaj.html',
    {

    })  

def dodaj(request):
    return render(request, 'dodaj.html',
    {

    })      