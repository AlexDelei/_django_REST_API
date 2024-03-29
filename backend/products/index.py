import algoliasearch_django as alg
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]
    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'