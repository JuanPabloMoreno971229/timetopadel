from django.urls import path
from .views import TorneoListView, TorneoDetailView


urlpatterns = [
    path('', TorneoListView.as_view(), name="home"),
]

torneo_patterns = ([
    path('<int:pk>/<slug:slug>/', TorneoDetailView.as_view(), name='torneo'),
], 'torneos')