from .import views
from beta.views import homepage, student_list, student_marks
from django.urls import path

urlpatterns = [
    path("", views.homepage, name = 'Homepage'),
    path("student_list/", views.student_list, name = 'Student List'),
    path("student_marks/", views.student_marks, name= 'Marks'),
]