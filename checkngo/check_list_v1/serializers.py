from .models import Category, Item
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = "__all__"

