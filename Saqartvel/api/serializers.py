from rest_framework import serializers
from api.models import Category, Subcategory, Venue, User


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(required=False, read_only=True, slug_field='title')

    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'slug', 'category']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'slug']


class CategoryDetailSerializers(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'icon', 'title', 'slug', 'subcategories']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'include_subcategories' in self.context and self.context['include_subcategories']:
            subcategories_data = Subcategory.objects.filter(category=instance)
            serialized_subcategories = SubcategorySerializer(subcategories_data, many=True).data
            ret['subcategories'] = serialized_subcategories
        return ret


class VenuesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class SubcategoryDetailSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(required=False, read_only=True, slug_field='title')
    venues = VenuesSerializers(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'include_venues' in self.context and self.context['include_venues']:
            venues_data = Venue.objects.filter(subcategory=instance)
            serialized_venues = VenuesSerializers(venues_data, many=True).data
            ret['subcategories'] = serialized_venues
        return ret


class SubcategoryCreateSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(required=False, queryset=Category.objects.all(), slug_field='title')

    class Meta:
        model = Subcategory
        fields = '__all__'

    def create(self, validated_data):
        subcategory = Subcategory.objects.create(**validated_data)
        cat, _ = Category.objects.get_or_create(title=validated_data['category'])
        subcategory.save()
        return subcategory


class VenuesListSerializers(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(required=False, read_only=True, slug_field='title')

    class Meta:
        model = Venue
        fields = ['id', 'title', 'slug', 'subcategory']


class VenuesCreateSerializers(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(required=False, queryset=Subcategory.objects.all(), slug_field='title')

    class Meta:
        model = Venue
        fields = '__all__'

    def create(self, validated_data):
        venue = Venue.objects.create(**validated_data)
        subcategory, _ = Subcategory.objects.get_or_create(title=validated_data['subcategory'])
        venue.save()
        return venue


class VenuesDetailSerializers(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(required=False, read_only=True, slug_field='title')

    class Meta:
        model = Venue
        fields = '__all__'
