from rest_framework import generics

from user.serializers import UserSerializer


# generics.CreateAPIView premade from DRF
# only needs the serializer of the model that we are using
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
