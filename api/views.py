from django.http import JsonResponse


def estudantesView(request):
    estudantes =  {
        'id': 1,
        'nome': 'Bruno Molina',
        'TI': 'TI'
    }
    return JsonResponse(estudantes)




