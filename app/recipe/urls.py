from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# feature of DRF
# https://www.django-rest-framework.org/api-guide/routers/
# api/recipe/tags/
# api/recipe/tags/<id> etc...
# what it will do is auto generate url for the router
# https://stackoverflow.com/questions/37661868/how-to-use-router-in-django-rest-not-for-viewsets-but-for-generic-views
# will only work with DRF viewset due to how it works

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

# this allows you to register app name for reverse('recipe:Tags')
app_name = 'recipe'

urlpatterns = [path('', include(router.urls))]
