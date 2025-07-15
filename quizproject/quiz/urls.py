from django.urls import path
from . import views

urlpatterns = [
    path('', views.paragraph_submission, name='paragraph_submission'),
    path('<int:quiz_id>/', views.generate_quiz, name='generate_quiz'),
]
