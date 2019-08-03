from django.contrib import admin
from .models import StudentCon
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_nu','dob','country','status']

admin.site.register(StudentCon,StudentAdmin)
