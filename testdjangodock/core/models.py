from django.db import models

#Create your models here
#On fait la database object appelé TodoList
class TodoList(models.Model):
    #On définit les attributs de todolist
    #Quand on met un attribut 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    #On veut faire en sorte que model soit dans la todolist
    #Python ne connait pas Todo, donc on dit que c'est un ForeignKey
    #on_delete, ça veut dire que si on détruit todolist, cela détruit tout les items
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

