from django.urls import path
from .views import HelloWorld,book_list,book_detail,book_create

urlpatterns = [
    path('hello/',HelloWorld.as_view()),
    #path('hello/<str:name>/',hello),

    path('books/', book_list, name='books_view'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/create', book_create, name='book_create')
]