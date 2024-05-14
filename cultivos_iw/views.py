from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate, login



@method_decorator(login_required, name='dispatch')
class Index(View):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivos_iw/index.html'
    success_url = reverse_lazy('cultivos_iw:index')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        cultivos = Cultivo.objects.all()
        return render(request, self.template_name, {'form': form, 'cultivos': cultivos})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    def delete(self, request, cultivo_id):
        cultivo = get_object_or_404(Cultivo, pk=cultivo_id)
        cultivo.delete()
        return redirect(self.success_url)
    
@method_decorator(login_required, name='dispatch')
class CultivoDetail(View):
   model = Cultivo
   template_name = 'cultivos_iw/details.html'
   
   def get(self, request, cultivo_id, *args, **kwargs):
        cultivo = get_object_or_404(Cultivo, id=cultivo_id)
        return render(request, self.template_name, {'cultivo': cultivo})

@method_decorator(login_required, name='dispatch')
class CultivoEditar(View):
    template_name = 'cultivos_iw/edit.html'
    form_class = CultivoForm
    success_url = reverse_lazy('cultivos_iw:index')
    def get(self, request, cultivo_id, *args, **kwargs):
        cultivo = get_object_or_404(Cultivo, id=cultivo_id)
        form = self.form_class(instance=cultivo)
        return render(request, self.template_name, {'form': form, 'cultivo': cultivo})

    def post(self, request, cultivo_id, *args, **kwargs):
        cultivo = get_object_or_404(Cultivo, id=cultivo_id)
        form = self.form_class(request.POST, request.FILES, instance=cultivo)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'cultivo': cultivo})
    
@method_decorator(login_required, name='dispatch')
class CultivoEliminar(View):
    template_name = 'cultivos_iw/index.html'

    def get(self, request, cultivo_id, *args, **kwargs):
        cultivo = get_object_or_404(Cultivo, id=cultivo_id)
        return render(request, self.template_name, {'cultivo': cultivo})

    def post(self, request, cultivo_id, *args, **kwargs):
        cultivo = get_object_or_404(Cultivo, id=cultivo_id)
        cultivo.delete()
        return JsonResponse({'message': 'Cultivo eliminado correctamente'}) 