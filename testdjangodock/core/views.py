from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import wiki
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ConnexionForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

#On récupère l'id envoyé dans l'URL
#Et on retourne le nom de l'élement de notre db avec l'ID 1
def searchid(request, id):
    ls = wiki.objects.get(id=id)
    return HttpResponse('<h1>%s</h1>' % (ls.article))


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(reverse(articles))
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(home))

def register(request):
    error = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            try :
                user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
                messages.error(request, "Vous êtes enregistrés")
                return redirect(home)
            except IntegrityError :
                messages.error(request, "Ce nom d'utilisateur est déjà pris.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', locals())

@login_required
def articles(request):
    """ Afficher tous les articles de notre blog """
    articles = wiki.manager.all() # Nous sélectionnons tous nos articles
    return render(request, 'articles.html', {'derniers_articles': articles})

@login_required
def lire(request, id):
    article = get_object_or_404(wiki, id=id)
    return render(request, 'lire.html', {'article':article})

@login_required
def ajout_fav(request, id):
    art = get_object_or_404(wiki, id=id)
    if art.favoris.filter(id=request.user.id).exists():
        art.favoris.remove(request.user)
    else:
        art.favoris.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def liste_fav(request):
    new = wiki.manager.filter(favoris=request.user)
    return render(request, 'favoris.html', {'new':new})

@login_required
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        wikis = wiki.manager.filter(article__contains=searched)
        return render(request, 'searchbar.html', {
            'searched':searched,
            'wikis': wikis
        })
    else:
        return render(request, 'searchbar.html', {})