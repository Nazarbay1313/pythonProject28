from rest_framework import fields, serializers

from product.models import Basket, Product


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'price', 'quantity',
                  'content', 'time_created', 'image', 'tags', 'is_published')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField
    total_sum = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum')

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()
