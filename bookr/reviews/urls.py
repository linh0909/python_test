from django.urls import path
from . import views
urlpatterns = [
 path('books/', views.book_list, name='books_list'),
]
