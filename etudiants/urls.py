
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_etudiants, name='liste_etudiants'),
    path('<int:id>/', views.detail_etudiant, name='detail_etudiant'),
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('<int:id>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('<int:id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
]
