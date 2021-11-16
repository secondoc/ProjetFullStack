from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item



def home(request):
    return render(request, 'index.html')

#On récupère l'id envoyé dans l'URL
#Et on retourne le nom de l'élement de notre db avec l'ID 1
def search(request, id):
    ls = TodoList.objects.get(id=id)
    items = ls.item_set.all()
    return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' % (ls.name, Item.text))