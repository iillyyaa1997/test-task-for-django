from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from user.models import User


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Role.ADMIN


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated and request.user.role == User.Role.ADMIN
