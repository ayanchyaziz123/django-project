from django.db import models


# Create your models here.

class Batch(models.Model):
    batchName = models.CharField(max_length=100, primary_key=True)


class Section(models.Model):
    batchName = models.ForeignKey(Batch, on_delete=models.CASCADE)
    sectionName = models.CharField(max_length=100, primary_key=True)


class Student(models.Model):
    sectionName = models.ForeignKey(Section, on_delete=models.CASCADE)
    studentId = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300)
    dateOfBirth = models.DateField(null=True)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    guardianPhone = models.CharField(max_length=200)


class Course(models.Model):
    sectionName = models.ForeignKey(Section, on_delete=models.CASCADE)
    courseCode = models.CharField(max_length=100)
    courseName = models.CharField(max_length=300, primary_key=True)


class Attendance(models.Model):
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendanceDate = models.DateField()
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
