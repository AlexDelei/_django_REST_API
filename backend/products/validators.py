from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(attrs):
    if "hello" in attrs.lower():
        raise serializers.ValidationError("hello is not allowed")

unique_product_title = UniqueValidator(queryset=Product.objects.all())