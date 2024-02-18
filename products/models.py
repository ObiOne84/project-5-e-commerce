from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    subcategory = models.ManyToManyField('Subcategory', blank=True)
    published_date = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    isbn_13 = models.CharField(max_length=13, null=True, blank=True)
    isbn_10 = models.CharField(max_length=10, null=True, blank=True)
    ave_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    ratings_count = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Book(Product):
    COVER_TYPES = [
        ('paperback', 'Paperback'),
        ('hardcover', 'Hardcover'),
    ]
    num_pages = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    cover = models.CharField(
        max_length=20, choices=COVER_TYPES, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Comic(Product):
    series = models.CharField(max_length=100, null=True, blank=True)
    age_rating = models.CharField(max_length=25, null=True, blank=True)
    illustrator = models.CharField(max_length=254, null=True, blank=True)
    cover_artist = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.title
