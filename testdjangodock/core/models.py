from django.db import models
from django.utils.translation import gettext as _

#Create your models here
#On fait la database object appelé TodoList
class wiki(models.Model):
    #On définit les attributs de todolist
    #Quand on met un attribut 
    article = models.CharField(_("Article"), max_length=255)
    nb_apparitions = models.IntegerField(_("Nombre d'apparitions"))
    moyenne_vus = models.FloatField(_("Moyenne du nombre de vus"))
    notes = models.CharField(_("Notes/about"), max_length=255)
    classe = models.CharField(_("Class"), max_length=255)
    def __str__(self):
        return self.article


#class Item(models.Model):
    #On veut faire en sorte que model soit dans la todolist
    #Python ne connait pas Todo, donc on dit que c'est un ForeignKey
    #on_delete, ça veut dire que si on détruit todolist, cela détruit tout les items
    #todolist = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    #text = models.CharField(max_length = 300)
    #complete = models.BooleanField()

    #def __str__(self):
    #    return self.text

