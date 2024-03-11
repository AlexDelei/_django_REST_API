from rest_framework import generics
from rest_framework import mixins
from rest_framework import authentication
from . models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api import *
from api.authentication import TokenAuthentication
from api.mixin import StaffEditorPermissionMixin


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    """
    Query's all data from our model storage
    creates new object's
    """
   # permission_classes = [permissions.DjangoModelPermissions]
    # this is a method of allowing authentified users to  access views

    queryset = Product.objects.all()
    # queryset is a collection of objects from database
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        create new object
        """
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            # set content's body to title if it has nothing
            content = title
        serializer.save(content=content)

    def get_queryset(self, *args, **kwargs):
        request = self.request
        qs =  Product.objects.all() 
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        print(f"------->{request.user}")
        print(f"----->{user}")
        return qs.filter(user=user)


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
    ):
    """
    Detailed listing of an object
    """
    queryset = Product.objects.all()
    # queryset selects all data from our model product
    serializer_class = ProductSerializer
    # then serializer_class specifies the serializer class to use in this class

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    """
    Deleting object of primary key given 'lookup_field'
    """
    queryset = Product.objects.all()
    # queryset selects all data from our model product
    serializer_class = ProductSerializer
    # then serializer_class specifies the serializer class to use in this class
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    """
    Update object in records
    """
    queryset = Product.objects.all()
    # queryset selects all data from our model product
    serializer_class = ProductSerializer
    # serializer specifies our serializer class.
    lookup_field = 'pk'
    # look_up field in django specifies the condition when querying a database

    def perform_update(self, serializer):
        """
        ofc update object and save 
        """
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.file


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    StaffEditorPermissionMixin,
    generics.GenericAPIView
    ):
    """
    This is a simple yet well defined class that will perform all CRUD operations
    within a single class
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def product_alt_view(request,  pk=None ,*args, **kwargs):
        """
        according to the http request that is either GET or POST , then this function will perform
        the crud operations
        """
        method = request.method  

        if method == "GET":
            # data will be provided either in detail view or list view
            # we will read the url args to fetch data on our database model
            # the look up key should be a primary key
            if pk is not None: # detail view
                obj = get_object_or_404(Product, pk=pk)

                data = ProductSerializer(obj, many=False).data
                # serializing the data and setting the defualt of many to false
                return Response(data) # list view
            
            queryset = Product.objects.all() 
            # fetches all the data and provides the list view provided the
            # primary key is valid
            data = ProductSerializer(queryset, many=True).data
            # serializing the data i.e  the process of converting complex data structures such as
            # objects or  data records that can be easily stored, converted and reconstructed
            #  this includes converting data ito JSON objects and vice versa
            return Response(data)
        
        if method == "POST":
            # create an item
            serializer = ProductSerializer(data=request.data)
            # converting data into JSON objects
            if serializer.is_valid(raise_exception=True):
                title = serializer.validated_data.get('title')
                content = serializer.validated_data.get('content') or None
                if content is None:
                    content = title
                serializer.save(content=content)
                return Response(serializer.data)
            # if the primary key provided is not valid then -> return statement with status_code 400
            return Response({"invalid": "not good data"}, status=400) 