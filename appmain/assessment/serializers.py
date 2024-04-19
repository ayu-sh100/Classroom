from rest_framework import serializers
from .models import Assignment,AssignmentTracker

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
    
class AssignmentTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTracker
        fields = '__all__'