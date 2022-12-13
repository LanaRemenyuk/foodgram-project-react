from .views import (IngredientViewSet,
                       RecipeViewSet,
                       TagViewSet,
                       CustomUserViewSet)
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = routers.DefaultRouter()
router_v1 = DefaultRouter()
router_v1.register(r'users', CustomUserViewSet, basename='users')
router_v1.register(r'tags', TagViewSet, basename='tags')
router_v1.register(r'ingredients', IngredientViewSet, basename='ingredients')
router_v1.register(r'recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]