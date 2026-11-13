
from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant, Filiere
from .forms import EtudiantForm


def liste_etudiants(request):
    etudiants = Etudiant.objects.select_related("filiere").all()
    filieres = Filiere.objects.all()

    filiere_id = request.GET.get("filiere")

    if filiere_id:
        etudiants = etudiants.filter(filiere_id=filiere_id)

    return render(request, "etudiants/liste.html", {
        "etudiants": etudiants,
        "filieres": filieres,
        "filiere_selectionnee": filiere_id,
    })


def detail_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    return render(request, "etudiants/detail.html", {
        "etudiant": etudiant
    })


def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()

    return render(request, "etudiants/formulaire.html", {
        "form": form,
        "titre": "Ajouter un étudiant"
    })


def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, "etudiants/formulaire.html", {
        "form": form,
        "titre": "Modifier un étudiant"
    })


def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    if request.method == "POST":
        etudiant.delete()
        return redirect('liste_etudiants')

    return render(request, "etudiants/supprimer.html", {
        "etudiant": etudiant
    })
