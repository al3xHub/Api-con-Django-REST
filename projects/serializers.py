from rest_framework import serializers
from .models import Project

class ProjectSerialized(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','description','technology', 'created_at')
        read_only_fields = ('created_at',) #Only we can read this field, NO create, NO delete etc....

