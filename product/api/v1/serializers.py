from rest_framework import serializers

from product import models


class DiscountedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiscountedProduct
        fields = [
            'id', 'image_uz', 'image_ru', 'product'
        ]


class ProductsSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField(method_name='get_discounted_price')

    class Meta:
        model = models.Product
        fields = [
            'id', 'image', 'name_uz', 'name_ru', 'price', 'discount_percentage', 'discounted_price'
        ]

    def get_discounted_price(self, obj):
        return (obj.price / 100) * obj.discount_percentage if obj.is_discount == True and obj.discount_percentage else 0


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = [
            'id', 'name_uz', 'name_ru'
        ]


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductBrand
        fields = [
            'id', 'name_uz', 'name_ru'
        ]


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = [
            'id', 'rgba_name', 'name'
        ]


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InfoName
        fields = [
            'id', 'name'
        ]


class TechInfoSerializer(serializers.ModelSerializer):
    infos = serializers.SerializerMethodField(method_name='get_infos')

    class Meta:
        model = models.TechnicalInfoName
        fields = [
            'id', 'name', 'infos'
        ]

    def get_infos(self, obj):
        infos = models.InfoName.objects.filter(tech_info__id=obj.id)
        return InfoSerializer(infos, many=True).data


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = [
            'id', 'rgba_name', 'name'
        ]


class ProductMediasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMedia
        fields = [
            'id', 'media'
        ]


class ProductTecInfoSerializer(serializers.ModelSerializer):
    tech_info_id = serializers.IntegerField(source='tech_info.id')
    tech_info = serializers.CharField(source='tech_info.name')
    info_name_id = serializers.IntegerField(source='info_name.id')
    info_name = serializers.CharField(source='info_name.name')

    class Meta:
        model = models.ProductInfo
        fields = ['tech_info_id', 'tech_info', 'info_name_id', 'info_name']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_id = serializers.IntegerField(source='category.id')
    brand_name = serializers.CharField(source='brand.name')
    brand_id = serializers.IntegerField(source='brand.id')
    discount_price = serializers.SerializerMethodField(method_name='get_discount_price')
    medias = serializers.SerializerMethodField(method_name='get_medias')
    colors = serializers.SerializerMethodField(method_name='get_colors')
    infos = serializers.SerializerMethodField(method_name='get_infos')

    class Meta:
        model = models.Product
        fields = [
            'id', 'category_name', 'category_id', 'brand_name', 'brand_id', 'name_uz', 'name_ru', 'price', 'image',
            'discount_percentage', 'is_discount', 'discount_price', 'medias', 'colors', 'infos',
        ]

    def get_discount_price(self, obj):
        return (obj.price / 100) * obj.discount_percentage if obj.is_discount == True and obj.discount_percentage else 0

    def get_colors(self, obj):
        return ColorsSerializer(obj.colors, many=True).data

    def get_medias(self, obj):
        return ProductMediasSerializer(models.ProductMedia.objects.filter(product=obj), many=True).data

    def get_infos(self, obj):
        infos = obj.infos.all()
        return ProductTecInfoSerializer(infos, many=True).data