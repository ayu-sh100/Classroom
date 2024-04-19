from django.db import models
from members.models import CustomUser
from django.utils import timezone
# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    summary = models.CharField(max_length=100)
    tags = models.CharField(max_length=255,default=None,blank=True,null=True)

class AssignmentTracker(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    percent_progress = models.PositiveIntegerField(default=0)
    score = models.FloatField(null=True, blank=True)
