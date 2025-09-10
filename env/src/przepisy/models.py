from django.db import models

# Create your models here.


class Przepisy(models.Model):
    IdPrzepisu = models.AutoField(primary_key=True)
    NazwaDania = models.CharField(max_length=128)
    AutorPrzepisu = models.CharField(max_length=120)
    RodzajKuchni = models.CharField(max_length=120)
    Produkty = models.CharField(max_length=12000)
    PrzepisDania = models.TextField(max_length=1200000000)
    def __str__(self):
        return self.NazwaDania

    class Meta:
         verbose_name = "Przepis"
         verbose_name_plural = "Przepisy"    


class Uzytkownicy(models.Model):
    IdUzytkownika = models.AutoField(primary_key=True)
    NazwaUzytkownika = models.CharField(max_length=120)
    haslo = models.CharField(max_length=120)
    def __str__(self):
        return self.NazwaUzytkownika

    class Meta:
         verbose_name = "Uzytkownik"
         verbose_name_plural = "Uzytkownicy"
                 


class Produkty(models.Model):
    IdProduktu = models.AutoField(primary_key=True)
    NazwaProduktu = models.CharField(max_length=120)
    IloscKalorii = models.IntegerField()
    def __str__(self):
        return self.NazwaProduktu

    class Meta:
         verbose_name = "Produkt"
         verbose_name_plural = "Produkty"
