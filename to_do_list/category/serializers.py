from .models import Category
from rest_framework import serializers
from user.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    
    owner = UserSerializer(read_only=True, many=False)
    
    class Meta:
        model = Category
        fields = ('name', 'description', 'owner')


    def create(self,validated_data):
        user = self.context.get('request').user
        category = Category.objects.create(owner=user, **validated_data)
        return category



