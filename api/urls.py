from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employees')


urlpatterns = [

    path('estudantes/', views.estudantesView),
    path('estudantes/<int:pk>/', views.estudantesDetailView),

    #path('employees/', views.Employees.as_view()),
    #path('employees/<int:pk>/', views.EmployeesDetail.as_view()),

    path('', include(router.urls))




]