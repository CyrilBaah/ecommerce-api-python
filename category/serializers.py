import rest_framework.serializers as serializers

from product.serializers import ProductListSerializer

from .models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "image", "slug"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "image", "products"]
