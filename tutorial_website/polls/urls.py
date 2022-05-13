from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/question/<int:question_id>', views.question, name='question'),
    path('polls/choice/<int:choice_id>', views.choice, name='choice')
]
