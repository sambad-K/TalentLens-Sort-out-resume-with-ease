from django.urls import path
from .views import VacancyListCreateView, VacancyRetrieveUpdateDestroyView

urlpatterns = [
    path('vacancies/', VacancyListCreateView.as_view(), name='listcreate'),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateDestroyView.as_view(), name='retrievedeleteupdate'),
]