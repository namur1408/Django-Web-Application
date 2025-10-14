from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['title', 'description']
    filter_horizontal = ('members',)
    ordering = ['start_date']

