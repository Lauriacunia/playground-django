from django.shortcuts import render
from myapp.models import Familiar
# Create your views here.

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "familiares.html", {"lista_familiares": lista_familiares})
