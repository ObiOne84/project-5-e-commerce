from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('add_comic/', views.AddComic.as_view(), name='add_comic'),
    path('edit/book/<int:product_id>/', views.edit_book, name='edit_book'),
    path('edit/comic/<int:product_id>/', views.edit_comic, name='edit_comic'),
    path(
        'delete/book/<int:product_id>/', views.delete_book, name='delete_book'
    ),
    path(
        'delete/comic/<int:product_id>/', views.delete_comic,
        name='delete_comic'
    ),
]
