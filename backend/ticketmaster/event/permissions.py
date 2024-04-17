from rest_framework import permissions

"""
This module defines the defines for the event api
"""


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    this defines the permissions to perform full CRUD on a events
    when the creator is authorized. Or Read-only when not
    """

    def has_object_permission(self, request, view, obj):
        """
        Defines Read-only permissions are allowed for any request
        Write permissions are only allowed to the creator of an event
        :param request: The current request instance.
        :param view: The view that the request was made to.
        :param obj: The object that the request is for.
        :return: True if the request has the necessary permissions, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated

        return obj.creator == request.user
