from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.note_list),
    path('note/<int:pk>/', views.note_detail)
]
