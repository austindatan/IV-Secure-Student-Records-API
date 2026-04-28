from rest_framework.permissions import BasePermission


class IsAdminGroup(BasePermission):
    """Allows access only to users in the 'Admin' group."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.groups.filter(name='Admin').exists()


class IsAdminOrFaculty(BasePermission):
    """Allows access to users in the 'Admin' or 'Faculty' groups."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.groups.filter(name__in=['Admin', 'Faculty']).exists()
