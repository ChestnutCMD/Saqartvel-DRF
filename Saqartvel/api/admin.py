from django.contrib import admin

from api.models import Category, Subcategory, Venue, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'icon')
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('id',)


admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category')
    list_display_links = ('title', 'category')
    search_fields = ('title',)
    readonly_fields = ('id',)
    list_filter = ('category',)


admin.site.register(Subcategory, SubcategoryAdmin)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'subcategory', 'url', 'description', 'telephone', 'address', 'images')
    list_display_links = ('title', 'subcategory', 'url', 'images')
    search_fields = ('title',)
    readonly_fields = ('id',)
    list_filter = ('subcategory',)


admin.site.register(Venue, VenueAdmin)
admin.site.register(User)
