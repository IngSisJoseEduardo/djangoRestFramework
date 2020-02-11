from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los propietarios de un objeto editarlo
    """
    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura están permitidos para cualquier solicitud,
        # así que siempre permitiremos solicitudes GET, HEAD u OPTIONS.

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user