from django.urls import path
from . import views

urlpatterns = [
   path('comment/', views.View_user_notes.as_view()),
   path('notes/', views.View_user_notes.as_view(), name='notes'),
   path('notes/add_note/', views.View_create_note.as_view(), name='add'),
]