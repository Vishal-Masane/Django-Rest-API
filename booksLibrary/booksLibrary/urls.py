"""
URL configuration for booksLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from bookApp.views import get_single_book, get_all_books, create_book
from bookApp.views import get_single_book, get_all_books, create_book
# from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/get-student/<int:id>/', views.get_student),
    # path('api/get-all-students/', views.get_all_students),
    # path('api/create-student/', views.create_student),


    path('api/book/get-single-book/<int:id>/', get_single_book),
    path('api/book/get-all-books/', get_all_books),
    path('api/book/create-book/', create_book),

]