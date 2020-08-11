from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        # fields are what will be translated to and from json
        # fields matches the models
        fields = ('email', 'password', 'name')
        # extra_kwargs for extra settings for fields
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # from DRF documentation and what you can overrides in serializers
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)