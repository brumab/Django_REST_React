from django.urls import path
from . import views

urlpatterns = [

    path('estudantes/', views.estudantesView),
    path('estudantes/<int:pk>/', views.estudantesDetailView),

    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),


]