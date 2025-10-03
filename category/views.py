from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product

from .models import Category
from .serializers import CategoryDetailSerializer, CategoryListSerializer

# Create your views here.


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)

    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)
