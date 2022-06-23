from django.urls import path
from .views import ListCurso, ViewCursoId, CreateCurso, DeleteCurso, ComisionesView, ComisionIdView
urlpatterns = [
    path('', ListCurso),
    path('<int:pk>', ViewCursoId),
    path('create/', CreateCurso),
    path('delete/<int:pk>', DeleteCurso),
    path('<slug:slug>/', ComisionesView),
    path('comision/<int:pk>', ComisionIdView),
]
