from django.urls import path
from . import views

urlpatterns = [
    path('faculty/', views.FacultyView.as_view()),
    path('faculty/<int:pk>/', views.FacultyView.as_view()),

    path('subject/', views.SubjectView.as_view()),
    path('subject/<int:pk>/', views.SubjectView.as_view()),

    path('group/', views.GroupView.as_view()),
    path('group/<int:pk>/', views.GroupView.as_view()),

    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentView.as_view()),

    path('teacher/', views.TeacherView.as_view()),
    path('teacher/<int:pk>/', views.TeacherView.as_view())

]
