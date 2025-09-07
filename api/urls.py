from django.urls import path
from . import views

urlpatterns = [

    path('estudantes/', views.estudantesView)

]