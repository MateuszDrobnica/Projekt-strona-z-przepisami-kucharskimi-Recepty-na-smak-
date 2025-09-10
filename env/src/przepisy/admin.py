from pyexpat import model
from django.contrib import admin
from .models import Przepisy, Uzytkownicy, Produkty
# Register your models here.



class UzytkownicyAdmin(admin.TabularInline):
    model = Uzytkownicy

class PrzepisyAdmin(admin.ModelAdmin):
    model = Przepisy

class ProduktyAdmin(admin.ModelAdmin):
    model = Produkty    

admin.site.register(Przepisy)
admin.site.register(Uzytkownicy)
admin.site.register(Produkty)
