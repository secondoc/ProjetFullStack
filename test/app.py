from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient


#Initialisation de Flask
app = Flask(__name__)

#Mise en place d'une instance de database
#le hostname dans le docker-compose.yml
#authSource = C'est pour dire admin ou user
#db = client => Le nom de la database afin de pouvoir initialiser le bon
def get_db():
    client = MongoClient(
        host='test_mongodb', 
        port=27017,
        username='root',
        password='pass',
        authSource='admin' 
        )  
    db = client["wiki_db"] 
    return db

#On met en place la route du Flask
@app.route('/')
def ping_server():
    return "<h1>Main page du projet FullStack</h1>"

#On met une nouvelle route pour pouvoir interroger la database et aller chercher les données
@app.route('/wiki/all')
#fonction afin de pouvoir récupérer les informations
#_wiki = db.wiki_tb.find() => Il permet d'aller chercher dans la table wiki_tb
def fetch_wiki(): 
    db = get_db()
    _wiki = db.wiki_tb.find() 
    wikis = [{'id' : wiki['id'], 'name' : wiki['name']} for wiki in _wiki]
    return jsonify({'wikis': wikis})

#On fait ça afin de pouvoir rechercher les articles dans l'URL 
#Ainsi on 
@app.route('/wiki')
def search_wiki():
    db = get_db()
    _wiki = db.wiki_tb.find() 
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return("Erreur : Indiquez une ID svp")
    results=[]
    for wiki in _wiki:
        if wiki['id'] == id:
            results.append({'id' : wiki['id'], 'name' : wiki['name']})
    return jsonify(results)

    

#Sert à lancer le serveur au lancement du programme
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)