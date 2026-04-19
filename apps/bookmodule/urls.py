
from django.urls import path
from apps.bookmodule import views
from . import views



urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('links/', views.links_page, name='links_page'),
 path('text_formatting', views.text_formatting, name='text_formatting'),
 path('listing', views.listing, name='listing'),
 path('tables', views.tables, name='tables'),
 path('search', views.search_books, name='search_books'),
 path('add/', views.add_book),
path('complex/query', views.complex_query, name="books.complex_query"),
path("lab8/task1/", views.task1, name="lab8_task1"),
path("lab8/task2/", views.task2, name="lab8_task2"),
path("lab8/task3/", views.task3, name="lab8_task3"),
path("lab8/task4/", views.task4, name="lab8_task4"),
path("lab8/task5/", views.task5, name="lab8_task5"),
path("lab8/task7/", views.task7, name="lab8_task7"),


]
