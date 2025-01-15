from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    student_id=models.IntegerField()

    def __str__(self):
        return self.name

#foreinkey

class mark(models.Model):
    student=models.ForeignKey('student',on_delete=models.CASCADE)
    total_mark=models.CharField(max_length=3)
    grade=models.CharField(max_length=3)

    def __str__(self):
        return self.grade

