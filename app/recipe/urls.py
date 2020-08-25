from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# feature of DRF
# api/recipe/tags/
# api/recipe/tags/<id> etc...
# what it will do is auto  generate url for the router

router = DefaultRouter()
router.register('tags', views.TagViewSet)

# this allows you to register app name for reverse('recipe:Tags')
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]