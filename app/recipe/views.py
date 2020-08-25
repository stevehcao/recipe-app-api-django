from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from recipe import serializers


# can use a different viewset instead of mixin as well
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        # this overrides queryset so you can have custom query here
        return self.queryset.filter(user=self.request.user).order_by('-name')

    # override create for custom
    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)
