from django.urls import path
from.views import CursoListView, AvaliacaoListView

urlpatterns = [
    path('cursos/', CursoListView.as_view(), name='curso-list'),
    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacao-list')
]
