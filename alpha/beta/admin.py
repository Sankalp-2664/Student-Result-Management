from django.contrib import admin
from .models import Mark, Student, Subject, Admin
# Register your models here.

admin.site.register(Mark)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Admin)
