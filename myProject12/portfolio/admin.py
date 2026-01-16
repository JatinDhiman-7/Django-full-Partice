from django.contrib import admin
from portfolio.models import Student,Profile

# admin.site.register(Student)
# admin.site.register(Profile)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age')
    search_fields=('name','city')
    list_filter=('age','city')
    ordering=("name",)
    