from datetime import timezone

from django.db import models
from authuser.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')],default='beginner')
    publish_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    is_active = models.BooleanField(default=True)
    Category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.title}-{self.id}--{self.short_description}"


class CourseDetail(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='details',null=True, blank=True)


    def __str__(self):
        return self.title



class CourseImage(models.Model):

    course = models.ForeignKey(Course, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='courses')