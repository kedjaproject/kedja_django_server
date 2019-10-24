from rest_framework.permissions import *


class IsSuperUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        print ("SU - has_object_permission:", request.user.is_superuser)
        return request.user.is_superuser

    def has_permission(self, request, view):
        print ("SU - has_permission:", request.user.is_superuser)
        return request.user.is_superuser


class ViewWall(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.public or obj.roles.filter(user=request.user).exists()


class ModifyWall(BasePermission):

    def has_object_permission(self, request, view, obj):
        # FIXME: roles can't be passed as a query here
        # It should check proper permissions instead
        return request.user.is_superuser or obj.roles.filter(user=request.user, roles=1).exists()
