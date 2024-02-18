from django.contrib import admin
from .models import Product, Category, Book, Comic


# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'author',
#         'price',
#         'description',
#         'category',
#         'published_date',
#         'publisher',
#         'isbn_13',
#         'isbn_10',
#         'ave_rating',
#         'ratings_count',
#         'image_url',
#         'image',
#     )

#     ordering = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory',)

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'num_pages', 'genre', 'cover',)


class ComicAdmin(admin.ModelAdmin):
    list_display = ('series', 'age_rating',
        'illustrator', 'cover_artist',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comic, ComicAdmin)

