from django.db import models
from members_app.models import Member

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    members = models.ManyToManyField(Member, related_name='courses')

    def __str__(self):
        return self.title

