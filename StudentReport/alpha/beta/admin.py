from django.contrib import admin
from .models import Students, Admins, Subjects, Marks, Course
# Register your models here.
admin.site.register(Students)
admin.site.register(Admins)
admin.site.register(Subjects)
admin.site.register(Marks)  
admin.site.register(Course) 

# class StudentAdmin(admin.ModelAdmin):
#     # Display student_id in the admin form
#     fields = ('student_id', 'first_name', 'last_name', 'class_name')
    
#     # Display student_id in the list view
#     list_display = ('student_id', 'first_name', 'last_name', 'class_name')

#     # Optional: Make student_id read-only (if it's auto-incrementing)
#     readonly_fields = ('student_id',)  # Makes student_id read-only

# admin.site.register(Student, StudentAdmin)
