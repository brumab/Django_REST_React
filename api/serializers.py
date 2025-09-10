from rest_framework import serializers
from estudantes.models import Estudantes
from employees.models import Employee
from blog.models import Blog



class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


