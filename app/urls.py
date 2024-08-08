from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
  path('',views.home,name="home"),
  path('add_note',views.add_note.as_view(),name="add_note"),
  path('note/<int:pk>',views.note.as_view(),name="note"),
   path('note-delete/<int:pk>',views.note_delete,name="delete"),
   
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signin/',views.Register.as_view(),name='signin')

  
]
