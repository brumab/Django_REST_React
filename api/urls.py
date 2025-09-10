from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employees')


urlpatterns = [

    path('estudantes/', views.estudantesView),
    path('estudantes/<int:pk>/', views.estudantesDetailView),

<<<<<<< HEAD
    #path('employees/', views.Employees.as_view()),
    #path('employees/<int:pk>/', views.EmployeesDetail.as_view()),

    path('',include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comentarios/', views.ComentariosView.as_view()),

    path('blogs/<int:pk>/', views.BlogsDetail.as_view()),
    path('comentarios/<int:pk>/', views.ComentariosDetail.as_view()),







=======
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
>>>>>>> 4e97bb7 (Resolve conflito e mescla tudo)


]