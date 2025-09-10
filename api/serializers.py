from rest_framework import serializers
from estudantes.models import Estudantes
from employees.models import Employee
<<<<<<< HEAD
from blog.models import Blog
=======
>>>>>>> 4e97bb7 (Resolve conflito e mescla tudo)



class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
<<<<<<< HEAD


=======
        
>>>>>>> 4e97bb7 (Resolve conflito e mescla tudo)
