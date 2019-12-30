from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, ItemViewSet


router = routers.DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("items", ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
