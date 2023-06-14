from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Torneo
from inscripcion.forms import InscripcionForm
from django.http import HttpResponseRedirect

class TorneoListView(ListView):
    model = Torneo

class TorneoDetailView(DetailView):
    model = Torneo
    form_class = InscripcionForm
    template_name = 'tu_template.html'  # Reemplaza 'tu_template.html' por el nombre de tu template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            torneo_id = self.kwargs['pk']
            inscripcion = form.save(commit=False)
            inscripcion.tournament_id = torneo_id  # Asignar el valor de la clave foránea
            inscripcion.save()
            return reverse(self.get_success_url())
        else:
            return print("Hola")

    def get_success_url(self):
        return reverse('torneos:torneo', args=[self.kwargs['pk'], self.kwargs['slug']]) + '?ok'

       
    
  
    
    
    

    
        

