from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission

from api.models import User


class AuthorizationPermission(BasePermission):
    message = 'Not allowed'

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False

        user = User.objects.get(pk=request.user.id)
        print(user.role)
        if user.role == 'admin':
            return True
        else:
            return False
