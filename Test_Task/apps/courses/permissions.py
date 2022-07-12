from rest_framework import permissions
from apps.accounts.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and User.objects.get(email=request.user.email).type == 'Moderator')


class IsReadOnlyRegular(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and User.objects.get(email=request.user.email).type == 'Regular':
            return True
        return False
