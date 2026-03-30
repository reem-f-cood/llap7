
from django.urls import path
from apps.bookmodule import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('links/', views.links_page, name='links_page'),
 path('text_formatting', views.text_formatting, name='text_formatting'),
 path('listing', views.listing, name='listing'),
 path('tables', views.tables, name='tables'),

]
