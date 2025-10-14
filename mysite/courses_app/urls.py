from django.urls import path
from .views import course_list, create_course, enroll_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('create/', create_course, name='create_course'),
    path('<int:course_id>/enroll/', enroll_course, name='enroll_course')
]
