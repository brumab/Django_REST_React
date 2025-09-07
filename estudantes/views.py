from django.http import HttpResponse


def estudantes(request):
    estudantes = [{'id': 1, 'nome': 'Bruno Molina', 'Anos': 40}]
    return HttpResponse(estudantes)

