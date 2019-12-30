from rest_framework.viewsets import ModelViewSet
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

