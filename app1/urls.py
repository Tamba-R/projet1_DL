from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('monsite/', myfunction, name='maroute'),
    #path('personnes/', liste_personnes, name='liste_personnes'),
    # Page principale avec tableau de toutes les personnes
    path('personnes/', views.liste_personnes, name='liste_personnes'),

    # Page de détails d'une personne selon son ID
    path('personnes/<int:id>/detail/', views.detail_personne, name='detail_personne'),

    # Page de modification d'une personne selon son ID
    path('personnes/<int:id>/modifier/', views.modifier_personne, name='modifier_personne'),
]

