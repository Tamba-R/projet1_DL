from django.shortcuts import render, get_object_or_404
from .models import Personne

# Create your views here.

#def myfunction(request):
#    return render(request,'index.html',{})

#def liste_personnes(request):
#    personnes = [
#        {'nom': 'Diallo', 'prenom': 'Fatou', 'age': 24, 'genre': 'F', 'adresse': 'Conakry'},
#        {'nom': 'Camara', 'prenom': 'Ibrahima', 'age': 28, 'genre': 'M', 'adresse': 'Kindia'},
#        {'nom': 'Bah', 'prenom': 'Mamadou', 'age': 30, 'genre': 'M', 'adresse': 'Labé'},
#    ]
#    return render(request, 'personnes.html', {'personnes': personnes})

from django.shortcuts import render, redirect
from .models import Personne
from .forms import PersonneForm

def liste_personnes(request):
    personnes = Personne.objects.all()

    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_personnes')  # Redirection pour éviter la double soumission
    else:
        form = PersonneForm()

    return render(request, 'personnes.html', {
        'personnes': personnes,
        'form': form
    })

# Vue pour afficher toutes les personnes dans un tableau
#def liste_personnes(request):
#    personnes = Personne.objects.all()  # Récupère toutes les personnes de la BDD
#    return render(request, 'personnes.html', {'personnes': personnes})

# Vue pour afficher les détails d'une personne selon son ID
def detail_personne(request, id):
    personne = get_object_or_404(Personne, pk=id)
    return render(request, 'detail.html', {'personne': personne})

# Vue pour accéder à la page de modification (formulaire ou simple affichage)
def modifier_personne(request, id):
    personne = get_object_or_404(Personne, pk=id)
    return render(request, 'modification.html', {'personne': personne})

