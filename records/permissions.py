from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import StudentRecord
from .serializers import StudentRecordSerializer

class IsAdminOrFaculty(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Admin', 'Faculty']).exists()

class StudentRecordViewSet(ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
