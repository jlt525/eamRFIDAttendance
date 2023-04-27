from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Registration import views

urlpatterns = [
    path('students/', views.StudentsList.as_view()),
    path('students/<int:pk>', views.StudentDetail.as_view()),
    path('sessions/', views.SessionsList.as_view()),
    path('sessions/<int:pk>', views.SessionDetail.as_view()),
    path('sessionstudent/', views.SessionstudentsList.as_view()),
    path('sessionstudent/<int:pk>', views.SessionstudentDetail.as_view()),
    path('register/', views.RegisterAttendance.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
