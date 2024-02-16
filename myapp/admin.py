from django.contrib import admin
from myapp.models import Resume

# @admin.register(Resume)
# class ResumeModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image',
#     'my_file']


from myapp.models import Employee
admin.site.register(Employee)
#Register your models here.
