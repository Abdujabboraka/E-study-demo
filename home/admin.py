from django.contrib import admin
from .models import Student, Course, Users
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'course__title')


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Users)