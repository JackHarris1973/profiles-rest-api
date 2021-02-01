from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit his/her own profile"""
        if request.method in permission.SAFE_METHODS:
            return True
        return obj.id == request.user.id
