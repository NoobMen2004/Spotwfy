from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Разрешаем безопасные методы всем
        if request.method in SAFE_METHODS:
            return True
        # Для остальных методов разрешаем только админам
        return request.user and request.user.is_staff
