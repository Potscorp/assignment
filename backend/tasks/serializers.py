from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'created_at')
        read_only_fields = ('id', 'created_at')
    
    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value
