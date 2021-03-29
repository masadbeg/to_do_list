from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category
from category.permissions import IsCategoryOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsCategoryOwnerOrReadOnly,IsAuthenticated)
    lookup_field='pk'



