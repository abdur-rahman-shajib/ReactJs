from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You must be the owner of this tourist place to update or delete it."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.creator.username == request.user.username
    