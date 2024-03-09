from rest_framework import permissions
"""
This module defines the defines for the reservation api
"""


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    this defines the permissions to perform full CRUD on a reservation
    when the creator is authorized. Or Read-only when not
    """
    def has_object_permission(self, request, view, obj):
        """
        Defines Read-only permissions are allowed for any request
        Write permissions are only allowed to the creator of a reservation
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user