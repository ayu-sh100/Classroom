from django.shortcuts import render
from rest_framework import generics
from .models import Assignment, AssignmentTracker 
from .serializers import AssignmentSerializer
from .serializers import AssignmentTrackerSerializer

class AssignmentCreateView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentTrackerCreateView(generics.CreateAPIView):
    queryset = AssignmentTracker.objects.all()
    serializer_class = AssignmentTrackerSerializer
