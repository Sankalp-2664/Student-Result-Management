from .import views
from beta.views import homepage, student_list, admin_dashboard, student_dashboard, add_student, delete_student, student_detail, view_subjects
from django.urls import path

urlpatterns = [
    path("", views.homepage, name = 'Homepage'),
    path("student_list/", views.student_list, name = 'student_list'),
    path("admin_dashboard/", views.admin_dashboard, name='admin_dashboard'),
    path("admin_add_student/", views.add_student, name = 'admin_student'),
    path("admin_delete_student/", views.delete_student, name = 'admin_delete_student'),
    path("student_dashboard/", views.student_dashboard, name='student_dashboard'),
    path("student_detail/", views.student_detail, name= 'student_detail'),
    path("view_subjects/", views.view_subjects, name='view_subjects'),
]