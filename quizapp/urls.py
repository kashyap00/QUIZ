from django.contrib import admin
from django.urls import path
from quizapp import views

urlpatterns = [
    
    path('', views.index, name='quizapp'),
    path('quiz',views.startquiz,name='quiz'),
    path('candidate',views.candidate,name='candidate'),
    path('questionmaker',views.questionmaker,name='questionmaker'),
    path('loginu',views.loginu,name='loginu'),
    path('logoutu',views.logoutu,name='logoutu'),
    path('loginus',views.loginus,name='loginus')


]
