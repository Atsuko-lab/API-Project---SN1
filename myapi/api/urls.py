from django.urls import path
from .views import *

urlpatterns = [
    path('study/accueil/', accueil_eleve),
    path('study/resume/', resume),
    path('study/explique/', explication),
    path('study/quiz/', quiz),
    path('study/question/', chat_with_gpt),
    
]

