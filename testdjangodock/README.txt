pip install django

------------------------Creation du projet Django--------------------------------------------

On va alors créer un projet django  
    django-admin startproject core .
Cela donne le dossier core et le fichier manage.py
Dans le dossier core on fait le fichier views.py
Et on l'importe dans le fichier url.py, et on fait un path vers views qui va représenter notre page d'accueil
    path('', views.home)

Le fichier views va surtout mettre en place le html
On a donc le dossier templates dans core

On met le core dans les installed_apps dans le fichier settings

On a juste à le lancer avec python manage.py runserver

------------------------Creation du DockerFile pour Django-------------------------------------

On met en place le requirements.txt
On peut choisir quel operating system on peut prendre pour faire tourner django
On va prendre une forme simple de linux.

Dans le DockerFile on copie/colle le requirements.txt dans l'espace de travail et on le lance afin d'installer ce qu'il faut
On va ensuite copier tout notre répertoire dans /app de Docker
Si on ne veut pas tout copier il faut faire un fichier .dockerignore. et mettre le nom des fichier à ignorer
On va lancer un code avec CMD afin de pouvoir lancer django dans docker
Mais on ajoute cette fois-ci une adresse (0.0.0.0:8000) afin de pouvoir accéder au serveur depuis notre navigateur web


Ainsi on a un container Docker 

------------------------Création des images-----------------------------------
On créer l'image avec
    docker build --tag python-django .

------------------------Création d'un container-------------------------------
On créer le conteneur avec 
    docker run --publish 8000:8000 python-django

on peut alors se connecter sur le 127.0.0.1:8000


Afin de pouvoir ajouter d'autres conteneurs, j'ai enlevé la commande CMD du Dockerfile, et je l'ai mis dans le docker-compose.yml
Comme ça on pourra avoir de multiple conteneurs

------------------------Mise en place de SQLlite--------------------------
    python manage.py migrate 
Ca veut dire qu'on a mis a jour les paramètres du fichier python, du coup on va pouvoir modifier manage.py

Un fichier model.py a été fait afin de pouvoir définir nos variable de base de données

Quand on fait une modification de Django il faut lui dire, on fait donc :
    python manage.py makemigrations core
Ainsi il indique qu'il a créé les modèles, et qu'il a sauvegardé les changement
Si on veut appliquer les changements il faut faire 
    python manage.py migrate
Pour accéder au shell du django il faut :
    python manage.py shell
A partir du shell on peut enregister la base de donnée : 
    from core.models import Item, Todolist 
Importe les objects
    t = TodoList(name="Liste1")
Sauvegarder dans la database
    t.save()
Afficher l'ensemble des Todolist
    TodoList.objets.all()
Afficher une Todolist par attribut  
    Todolist.objects.get(id=1)
Si on voir les items de la Todolist
    t.item_set_all()
Créer un item dans todolist 
    t.item_set.create(text="...")
