from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# feature of DRF
# api/recipe/tags/
# api/recipe/tags/<id> etc...
# what it will do is auto  generate url for the router
# https://www.django-rest-framework.org/api-guide/routers/

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

# this allows you to register app name for reverse('recipe:Tags')
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]