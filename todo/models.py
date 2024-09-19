from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField()


    def __str__(self):  ## fonction = message pour afficher nom du task dans l affichage et non pas sous forme "task object 1 "
        return self.name

