from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from .models import torneo
from inscripcion.forms import InscripcionForm
from django.http import HttpResponseRedirect

class TorneoListView(ListView):
    model = torneo

class TorneoDetailView(DetailView):
    model = torneo
    form_class = InscripcionForm
    template_name = 'core/torneo_detail.html'  # Reemplaza 'torneo_detail.html' por tu plantilla de detalle

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
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        torneo_id = self.kwargs['pk']
        return reverse('torneos:detalle', args=[torneo_id]) + '?ok'
