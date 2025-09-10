from django.contrib import admin
from django.urls import path
from przepisy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('index/', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('uzytkownicy/', views.uzytkownicy, name='uzytkownicy'),
    path('szukaj/', views.szukaj, name='szukaj'),
    path('dodaj/', views.dodaj_przepis, name='dodaj'),
    path('mieso/', views.mieso, name='mieso'),
    path('weganskie/', views.weganskie, name='weganskie'),
    path('wegetarianskie/', views.wegetarianskie, name='wegetarianskie'),
    path('jarskie/', views.jarskie, name='jarskie'),
    path('bezglutenowe/', views.bezglutenowe, name='bezglutenowe'),

]
