#from django.http import JsonResponse
from estudantes.models import Estudantes
from .serializers import EstudantesSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import generics, mixins




@api_view(['GET', 'POST'])
def estudantesView(request):
    if request.method == 'GET':
        # Obter todos os dados da tabela estudantes
        estudantes = Estudantes.objects.all()
        serializer = EstudantesSerializer(estudantes, many=True) 

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = EstudantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def estudantesDetailView(request, pk):
    try:
        estudante = Estudantes.objects.get(pk=pk)
    except Estudantes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstudantesSerializer(estudante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EstudantesSerializer(estudante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estudante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


#class Employees(APIView):
    #def get(self, request):
        #employees = Employee.objects.all()
        #serializer = EmployeeSerializer(employees, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    #def post(self, request):
        #serializer = EmployeeSerializer(data=request.data)
        #if serializer.is_valid():
           #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class EmployeesDetail(APIView):
    #def get_object(self, pk):
        #try:
            #return Employee.objects.get(pk=pk)
        #except Employee.DoesNotExist:
            #raise Http404

    #def get(self, request, pk):
        #employee = self.get_object(pk)
        #serializer = EmployeeSerializer(employee)
        #return Response(serializer.data, status=status.HTTP_200_OK)

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class EmployeesDetail(generics.GenericAPIView):
    pass


##bruno Molina 2025