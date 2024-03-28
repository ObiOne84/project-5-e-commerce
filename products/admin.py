from django.contrib import admin
from .models import Product, Category, Book, Comic, Subcategory, Review


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    list_display = ('id', 'name', 'product_type',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'num_pages', 'genre', 'cover',)


class ComicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'series', 'age_rating',
                    'illustrator', 'cover_artist',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
                    'body', 'created_on', 'approved',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comic, ComicAdmin)
admin.site.register(Review, ReviewAdmin)
