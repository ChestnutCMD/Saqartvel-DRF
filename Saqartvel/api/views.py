from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.permissions import AuthorizationPermission
from api.serializers import *
from api.models import Category, Subcategory, Venue


class CategoryListView(ListAPIView):
    """ Список всех категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryCreateView(CreateAPIView):
    """ Создание категории """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AuthorizationPermission]


class CategoryDetailView(RetrieveAPIView):
    """ Вывод категории по ID """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_subcategories'] = True
        return context


class CategorySlugView(RetrieveAPIView):
    """ Вывод категории по слагу """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_subcategories'] = True
        return context


class CategoryUpdateView(UpdateAPIView):
    """ Обновление категории """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AuthorizationPermission]


class CategoryDeleteView(DestroyAPIView):
    """ Удаление категории """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AuthorizationPermission]

# Subcategory


class SubcategoryListView(ListAPIView):
    """ Список всех подкатегорий """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryListSerializer


class SubcategoryCreateView(CreateAPIView):
    """ Создание подкатегории """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryCreateSerializers
    permission_classes = [AuthorizationPermission]


class SubcategoryDetailView(RetrieveAPIView):
    """ Вывод подкатегории по ID"""
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryDetailSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_venues'] = True
        return context


class SubcategorySlugView(RetrieveAPIView):
    """ Вывод подкатегории по слагу """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryDetailSerializers
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_venues'] = True
        return context


class SubcategoryUpdateView(UpdateAPIView):
    """ Обновление подкатегории """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [AuthorizationPermission]


class SubcategoryDeleteView(DestroyAPIView):
    """ Удаление подкатегории """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [AuthorizationPermission]

# Venue


class VenueListView(ListAPIView):
    """ Вывод всех заведений """
    queryset = Venue.objects.all()
    serializer_class = VenuesListSerializers


class VenueCreateView(CreateAPIView):
    """ Создание заведения"""
    queryset = Venue.objects.all()
    serializer_class = VenuesCreateSerializers
    permission_classes = [AuthorizationPermission]


class VenueDetailView(RetrieveAPIView):
    """ Вывод заведения по ID """
    queryset = Venue.objects.all()
    serializer_class = VenuesDetailSerializers


class VenueSlugView(RetrieveAPIView):
    """ Вывод заведения по слагу """
    queryset = Venue.objects.all()
    serializer_class = VenuesDetailSerializers


class VenueUpdateView(UpdateAPIView):
    """ Обновление заведения """
    queryset = Venue.objects.all()
    serializer_class = VenuesDetailSerializers
    permission_classes = [AuthorizationPermission]


class VenueDeleteView(DestroyAPIView):
    """ Удаление заведения """
    queryset = Venue.objects.all()
    serializer_class = VenuesListSerializers
    permission_classes = [AuthorizationPermission]
