from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import StudentRecord
from .serializers import StudentRecordSerializer
from .permissions import IsAdminGroup, IsAdminOrFaculty


class StudentRecordViewSet(ModelViewSet):
    serializer_class = StudentRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name__in=['Admin', 'Faculty']).exists():
            return StudentRecord.objects.all()
        return StudentRecord.objects.filter(owner=user)

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminGroup]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
