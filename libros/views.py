from django.shortcuts import render
from rest_framework import viewsets
from .models import Libro
from .serializer import LibroSerializer

# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

