  
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('example/',views.example,name='example'),
    path('fileload/', views.fileload, name='fileload'),
    path('viewfile/', views.viewfile, name='viewfile'),
    path('search_file/',views.search_file, name='search_file'),
    path('contact/', views.contact,name='contact'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('viewfile/<int:id>', views.delete_doc, name='delete_doc'),
   ]

