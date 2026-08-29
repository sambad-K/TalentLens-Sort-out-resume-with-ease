from django.shortcuts import render

# Create your views here.
from .models import Vacancy
from rest_framework import generics
from .serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .pagination import VacancyPagination
class VacancyListCreateView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = VacancyPagination
class VacancyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VacancySerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        if (self.request.user.is_superuser):
            return Vacancy.objects.filter(posted_by=self.request.user)
        else:
            return Response({"message": "You do not have permission to access this resource."}, status=status.HTTP_403_FORBIDDEN)
        