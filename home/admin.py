
from django.contrib import admin
from .models import Batch, Course, Attendance
from .models import Section
from .models import Student, Contact


# Register your models here.

admin.site.register(Batch)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Contact)

