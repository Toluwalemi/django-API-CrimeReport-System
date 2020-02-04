from rest_framework import permissions


class IsReporterOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        # if request.method in permissions.SAFE_METHODS:
        #     return False

        # Write permissions are only allowed to the author of a post
        return obj.reporter == request.user
