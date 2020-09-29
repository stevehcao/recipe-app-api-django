from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


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


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    # what this does for MTM fields to list only PK of the
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'ingredients',
            'tags',
            'time_minutes',
            'price',
            'link',
        )
        read_only_fields = ('id', )
        # prevent PK from changing


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a receipe detail"""
    # override the igredients and tags so that you read all fields
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipe"""

    class Meta:
        model = Recipe
        # only to accept image field for this serializer
        fields = ('id', 'image')
        read_only_fields = ('id', )
