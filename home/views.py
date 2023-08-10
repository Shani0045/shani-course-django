from django.shortcuts import render
from datetime import datetime
from .models import Course, CourseContent, CourseDetails

# Create your views here.

def home(request):
    context = {}
    course_qs = Course.objects.all()
    context["courses"] = course_qs
    return render(request ,"pages/home.html", context)

def about(request):
    context = {}
    course_qs = Course.objects.all()
    context["courses"] = course_qs
    return render(request ,"pages/about.html", context)

def contact(request):
    context = {}
    course_qs = Course.objects.all()
    context["courses"] = course_qs
    return render(request ,"pages/contact.html", context)

def content(request, id):
    context = {}
    course_qs = Course.objects.all()
    context["courses"] = course_qs
    course_content_qs = CourseContent.objects.filter(course_id=id)
    context["contents"] = course_content_qs
    
    return render(request ,"pages/content.html", context)


def content_description(request, id):
    context = {}
    course_qs = Course.objects.all()
    context["courses"] = course_qs

    try:
        content_description_qs = CourseDetails.objects.get(id=id)
    except CourseDetails.DoesNotExist:
        content_description_qs = None
        
    context["descriptions"] = content_description_qs

    return render(request ,"pages/content-descriptions.html", context)