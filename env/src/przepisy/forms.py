from django import forms

class DodajPrzepis(forms.Form):
    NazwaDania = forms.CharField(label ='Nazwa Dania', max_length=120)
    AutorPrzepisu = forms.CharField(label ='Autor Przepisu', max_length=120)
    RodzajKuchni =  forms.CharField(label ='Rodzaj Kuchni', max_length=120)
    Produkty =  forms.CharField(label ='Produkty', max_length=120000)
    PrzepisDania = forms.CharField(label ='Opis', max_length=12000000000)