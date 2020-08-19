from django.contrib.auth import get_user_model, authenticate
# translation module which output to screen to convert text language
from django.utils.translation import ugettext_lazy as _

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

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        # pop must provide default value
        # pop is like get but after it retrieves it, it will remove from dictionary after
        # pop is built in dictionary function, optionally provide
        password = validated_data.pop('password', None)
        # super() will call the ModelSerializer update
        # super() is using functions from the parent class
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    # django validate custom for email
    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        # authenticate from top
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password)
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs