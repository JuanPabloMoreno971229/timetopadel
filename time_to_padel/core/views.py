from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
<<<<<<< HEAD
from django.shortcuts import redirect
from django.urls import reverse
from .models import torneo
=======
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Torneo
>>>>>>> 5c9224eb340f7b3ba76ab05f3fb7f867528c0d95
from inscripcion.forms import InscripcionForm
from django.http import HttpResponseRedirect

class TorneoListView(ListView):
    model = Torneo

class TorneoDetailView(DetailView):
    model = Torneo
    form_class = InscripcionForm
<<<<<<< HEAD
    template_name = 'core/torneo_detail.html'  # Reemplaza 'torneo_detail.html' por tu plantilla de detalle
=======
    template_name = 'tu_template.html'  # Reemplaza 'tu_template.html' por el nombre de tu template
>>>>>>> 5c9224eb340f7b3ba76ab05f3fb7f867528c0d95

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            torneo_id = self.kwargs['pk']
            inscripcion = form.save(commit=False)
            inscripcion.tournament_id = torneo_id
            inscripcion.save()
            return reverse(self.get_success_url())
        else:
<<<<<<< HEAD
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        torneo_id = self.kwargs['pk']
        return reverse('torneos:detalle', args=[torneo_id]) + '?ok'
=======
            return print("Hola")

    def get_success_url(self):
        return reverse('torneos:torneo', args=[self.kwargs['pk'], self.kwargs['slug']]) + '?ok'

       
    
  
    
    
    

    
        

>>>>>>> 5c9224eb340f7b3ba76ab05f3fb7f867528c0d95
