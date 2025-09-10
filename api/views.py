#from django.http import JsonResponse
from estudantes.models import Estudantes
from .serializers import EstudantesSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import generics, mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from blog.models import Blog, comentario
from blog.serializers import BlogSerializer, ComentarioSerializer
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter








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
            #return Response(serializer.data, status=status.HTTP_200_OK)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #def delete(self, request, pk):
         #employee = self.get_object(pk)
         #employee.delete()
         #return Response(status=status.HTTP_204_NO_CONTENT)



class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""""

# Mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

# Mixins    
class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def  delete(self, request, pk):
        return self.destroy(request, pk)
    

# Generics
class Employees(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Generics
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

"""

#class EmployeeViewSet(viewsets.ViewSet):
#    def list(self, request):
#        quesryset = Employee.objects.all()
#        serializer = EmployeeSerializer(quesryset, many=True)
#        return Response(serializer.data)
#    
#    def create(self, request):
#        serializer = EmployeeSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors)
#    
#    def retrieve(self, request, pk=None):
#        employee = get_object_or_404(Employee, pk=pk)
#        serializer = EmployeeSerializer(employee)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    
#    def update(self, request, pk=None):
#        employee = get_object_or_404(employee, pk=pk)
#        serializer = EmployeeSerializer(employee, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors.erros)
#    
#    def delete(self, request, pk=None):
#        employee = get_object_or_404(Employee, pk=pk)
#        employee.delete()
#        return Response(status==status.HTTP_204_NO_CONTENT)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter


class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['Blog_title', 'Blog_body']
    ordering_fields = ['id', 'Blog_title']


class ComentariosView(generics.ListCreateAPIView):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer



class BlogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'



class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer
    lookup_field = 'pk'


class EmployeesDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    