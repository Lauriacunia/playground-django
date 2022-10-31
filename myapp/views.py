from django.shortcuts import render
from myapp.models import Familiar
from myapp.forms import Buscar , FamiliarForm
from django.views import View 


def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):

    form_class = Buscar # form que definimos en el archivo forms.py
    template_name = 'buscar.html'
    initial = {"nombre":""} # valor inicial del campo nombre

    def get(self, request):
        form = self.form_class(initial=self.initial) # inicializamos el formulario
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST) # carga los datos del formulario
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
