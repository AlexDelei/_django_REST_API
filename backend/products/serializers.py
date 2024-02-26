from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
from .validators import validate_title
from .UserPublicSerializer import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    # url_2 = serializers.HyperlinkedIdentityField(
     #   view_name='product-detail',
      #  lookup_field='pk'
    #)
    # email = serializers.EmailField(write_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title])
    url = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)


    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_disc'
        ]

    def validate_title(self, attrs):
        qs = Product.objects.filter(title__exact=attrs)
        if qs.exists():
            raise serializers.ValidationError(f"{attrs} already a product name")
        return attrs

   # def create(self, validated_data):
        #return Product.objects.create(**validated_ta)
        #email = validated_data.pop('email')
        #obj = super().create(validated_data)
        #print(email, obj)
        #return obj
    def get_url(self, obj):
       # return f"/api/v2/products/{obj.id}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={"pk": obj.pk}, request=request)
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={"pk": obj.pk}, request=request)