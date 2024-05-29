from django.contrib import admin
from .models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'registration_id','section', 'studying_year')
    search_fields = ('registration_id','first_name','last_name','course', 'section', 'studying_year', 'graduation','email_address', 'phone_number')


admin.site.register(Student, StudentAdmin)
