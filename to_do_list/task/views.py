from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet

class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
