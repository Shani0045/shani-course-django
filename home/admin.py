from django.contrib import admin
from home.models import Course, CourseContent, CourseDetails
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content")

@admin.register(CourseDetails)
class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ("id", "descriptions")