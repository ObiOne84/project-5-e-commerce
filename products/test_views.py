from django.test import TestCase
from django.urls import reverse
from .models import Book, Comic, Category, Subcategory


class ProductDetailViewTest(TestCase):
    def setUP(self):
        self.category = Category.objects.create(name='Fiction')
        self.subcategory = Subcategory.objects.create(name='Sci-Fi')
        self.book = Book.objects.create(
            title='Test Book',
            author='Book Author',
            description="Great book",
            category=self.category,
            subcategory=self.subcategory,
        )
        self.book = Comic.objects.create(
            title='Comic Book',
            author='Comic Author',
            description="Great comic",
            category=self.category,
            subcategory=self.subcategory,
        )

    def text_existing_product_detail(self):
        # Test if the view renders correctly for exisiting products
        response = self.client.get(
            reverse('product_detail', args=[self.book.pk])
        )
        self.assertEqual(response.status_code, 200)
