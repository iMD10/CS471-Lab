from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links', views.viewlinks, name="html5.links"),
 path('html5/text/formatting', views.texts, name="html5.texts"),
 path('html5/listing', views.listing,name="html5.listing"),
 path('html5/tables', views.tables,name="html5.tables"),
 path('search', views.search, name='books.search'),
#  path('simple/query', views.simple_query,name="books.simple_query"),
#  path('complex/query', views.complex_query,name="books.simple_query"),
#  path('lab8/task1', views.task1, name='books.lab8.task1'),
#  path('lab8/task2', views.task2 , name='books.lab8.task2'),
#  path('lab8/task3', views.task3 , name='books.lab8.task3'),
#  path('lab8/task4', views.task4 , name='books.lab8.task4'),
#  path('lab8/task5', views.task5 , name='books.lab8.task5'),
#   path('lab8/task7', views.task7 , name='books.lab8.task7'),
 path('lab9/task1', views.task1 , name='books.lab9.task1'),
 path('lab9/task2', views.task2 , name='books.lab9.task2'),
 path('lab9/task3', views.task3 , name='books.lab9.task3'),
 path('lab9/task4', views.task4 , name='books.lab9.task4'),
 path('lab9/task5', views.task5 , name='books.lab9.task5'),
 path('lab9/task6', views.task6 , name='books.lab9.task6'),
 path('lab10_part1/listbooks', views.CRUD_list_books, name='books.lab10.listbooks'),
 path('lab10_part1/addbook', views.CRUD_add_book, name='books.lab10.addbook'),
 path('lab10_part1/editbook/<int:bid>', views.CRUD_edit_book, name='books.lab10.editbook'),
 path('lab10_part1/deletebook/<int:bid>', views.CRUD_delete_book, name='books.lab10.deletebook'),
 
 path('lab10_part2/addbook', views.DjCRUD_add_book, name='books.lab10_2.addbook'),
 path('lab10_part2/editbook/<int:bid>', views.DjCRUD_edit_book, name='books.lab10_2.editbook'),
 path('lab10_part2/deletebook/<int:bid>', views.DjCRUD_delete_book, name='books.lab10_2.deletebook'),




 







]