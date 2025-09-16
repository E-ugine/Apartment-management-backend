# users/permissions.py
from rest_framework.permissions import BasePermission

class IsLandlord(BasePermission):
    """
    Allows access only to users with role = 'landlord'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "landlord"


class IsCaretaker(BasePermission):
    """
    Allows access only to users with role = 'caretaker'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "caretaker"


class IsTenant(BasePermission):
    """
    Allows access only to users with role = 'tenant'
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "tenant"


class IsLandlordOrCaretaker(BasePermission):
    """
    Allows access to users with role in {landlord, caretaker}
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.role in {"landlord", "caretaker"}
        )
