from django.db import models
from django.db.models.constraints import UniqueConstraint


class Category(models.Model):
    PRODUCT_CHOICES = [
        ('comic', 'Comic'),
        ('book', 'Book'),
        ('product', 'Product'),
    ]

    name = models.CharField(max_length=254)
    product_type = models.CharField(
        max_length=20, choices=PRODUCT_CHOICES, null=True,
        blank=True, default=None
    )
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Subcategory(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subcategories'
        constraints = [
            UniqueConstraint(
                fields=['name', 'category'],
                name='unique_subcategory_per_category'
            )
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL,
        default=19
    )
    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=True, on_delete=models.SET_NULL
    )
    published_date = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    isbn_13 = models.CharField(max_length=13, null=True, blank=True)
    isbn_10 = models.CharField(max_length=10, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0
    )
    ratings_count = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_in_wishlist(self, user):
        return self in user.wishlist.items.all()


class Book(Product):
    COVER_TYPES = [
        ('paperback', 'Paperback'),
        ('hardcover', 'Hardcover'),
    ]
    subtitle = models.CharField(max_length=254, null=True, blank=True)
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


# Source: Blog walkthrough project
class Review(models.Model):
    product = models.ForeignKey(
            Product, on_delete=models.CASCADE, related_name='reviews'
            )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
