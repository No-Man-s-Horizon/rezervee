from rest_framework.permissions import BasePermission


# Has_permission is read, has_object_permission is write permission
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object."

    # If you want to allow only owner users or admin to perform a certain action
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser
