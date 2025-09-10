from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_nome = models.CharField(max_length=50)

    designacao = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_nome
    

    #BRUNO 3:00 2025

    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_nome

