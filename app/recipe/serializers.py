from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id', )


# ingredient serialzers


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredients"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id', )
