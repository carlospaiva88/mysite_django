from django.http import HttpResponse
from django.views import generic

class Exercicio8View(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Exercicio Modulo 8')