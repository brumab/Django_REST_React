from django.db import models

class Estudantes(models.Model):
    Estudante_id = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    Ramo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

#BRUNO 5:00 2025