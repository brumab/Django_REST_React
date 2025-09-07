from django.http import HttpResponse


def Estudantes(request):
    Estudantes = [{'id': 1, 'nome': 'Bruno Molina', 'Anos': 40}]
    return HttpResponse(Estudantes)

