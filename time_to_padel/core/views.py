from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import torneo
from inscripcion.forms import InscripcionForm
from django.http import HttpResponseRedirect

class TorneoListView(ListView):
    model = torneo

class TorneoDetailView(DetailView):
    model = torneo
    form_class = InscripcionForm

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
            return HttpResponse('Hola, mundo!')
        else:
            return HttpResponse('Hola, mundo =(!')
    
    
    

    
        

