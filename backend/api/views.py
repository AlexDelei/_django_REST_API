import json
from django.http import JsonResponse # responsible for returning json

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    Our API view
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        instacnce = serializer.save()
        print(instacnce)
        return Response(serializer.data)
    
    
    
    
    
    
    
    
    
    #model_data = Product.objects.all().order_by("?").first()
    #data = request.data

    #instance = Product.objects.all().order_by("?").first()
    #data = {}
   
    #if instance:
        #data['id'] = model_data.id
        #data['title'] = model_data.title
        #data['content'] = model_data.content
        #data['price'] = model_data.price
        
        #data = (model_data, fields=['id', 'title', 'content', 'sale_disc'])
        # data = ProductSerializer(instance).data
        # turning model data into a dictionary representation with specified fields

    #return JsonResponse(data)






    # request -> HttpRequest  Django
    # request is an instance of the class HttpRequest
    # request.body
    #body = request.body
    # returns string byte of JSON data
    #data = {}
    #try:
    #    data = json.loads(body)
        # data is taken inform of a string in JSON object and converts it to a python dictionary
    #except:
    #    pass

    #print(data)
    #print(request.GET) # url query parameters
    #print(request.POST)
    #data['params'] = dict(request.GET)
    #data['headers'] = dict(request.headers)
    #data['content_type'] = request.content_type

    #return JsonResponse(data)

