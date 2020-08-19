from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import AuthTokenSerializer, UserSerializer


# generics.CreateAPIView premade from DRF
# only needs the serializer of the model that we are using
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


# take this token and save somewhere to authenticate
# can save as a cookie and use later
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    # this let's you see this endpoint for renderer class for ObtainAuthToken
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    # this is overriding the getting of a model
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user