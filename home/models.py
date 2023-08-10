from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False,blank=False)

    class Meta:
        db_table = "courses"

class CourseContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_content"

class CourseDetails(models.Model):
    id = models.AutoField(primary_key=True)
    descriptions = models.TextField()
    content_id = models.ForeignKey(CourseContent, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_details"


