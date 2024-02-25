from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('add_comic/', views.AddComic.as_view(), name='add_comic'),
    path('edit_book/<int:product_id>/', views.edit_book, name='edit_book'),
    path('edit_comic/<int:product_id>/', views.edit_comic, name='edit_comic'),
]
