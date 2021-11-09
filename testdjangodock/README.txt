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
