from django.shortcuts import render
from django.http import HttpResponse
from .models import wiki



def home(request):
    return render(request, 'index.html')

#On récupère l'id envoyé dans l'URL
#Et on retourne le nom de l'élement de notre db avec l'ID 1
def search(request, id):
    ls = wiki.objects.get(id=id)
    return HttpResponse('<h1>%s</h1>' % (ls.article))