from rest_framework import viewsets, mixins  # , generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe

from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)


# can use a different viewset instead of mixin as well
# class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                  mixins.CreateModelMixin):
#     """Manage tags in the database"""
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated, )
#     queryset = Tag.objects.all()
#     serializer_class = serializers.TagSerializer

#     def get_queryset(self):
#         """Return objects for the current authenticated user only"""
#         # this overrides queryset so you can have custom query here
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     # override create for custom
#     # serializer is passed in and save
#     def perform_create(self, serializer):
#         """Create a new ingredient"""
#         serializer.save(user=self.request.user)

# # view for ingredients can use viewsets and mixin or generic class view
# class IngredientViewSet(generics.ListCreateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer
#     permission_classes = [IsAuthenticated]

# can override various methods on the view class for complex queries
# def list(self, request):
# Note the use of `get_queryset()` instead of `self.queryset`
# queryset = self.get_queryset()
# serializer = IngredientSerializer(queryset, many=True)
# return Response(serializer.data)

# Refactored above
# class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                         mixins.CreateModelMixin):
#     """Manage ingredients in the database"""
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated, )
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer

#     def get_queryset(self):
#         """Return objects for the current authenticated user only"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self, serializer):
#         """Create a new ingredient"""
#         serializer.save(user=self.request.user)
