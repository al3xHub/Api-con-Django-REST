from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerialized

#what queries can they use
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerialized


