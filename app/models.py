from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    description = models.TextField()
    semester = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=100)
    due_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.assignment_name

class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.course}: {self.assignment} - {self.grade}"
