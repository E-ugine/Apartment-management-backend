from rest_framework import viewsets, permissions
from .models import Unit
from .serializers import UnitSerializer
from users.permissions import IsLandlord, IsCaretaker, IsTenant


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all().order_by('apartment_name', 'unit_number')
    serializer_class = UnitSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsLandlord()]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        role = getattr(user, 'role', None)

        # Scope by role
        if role == 'tenant':
            qs = qs.filter(tenant=user)

        # Simple filters
        apartment_name = self.request.query_params.get('apartment_name')
        unit_number = self.request.query_params.get('unit_number')
        is_occupied = self.request.query_params.get('is_occupied')
        tenant_id = self.request.query_params.get('tenant_id')

        if apartment_name:
            qs = qs.filter(apartment_name__icontains=apartment_name)
        if unit_number:
            qs = qs.filter(unit_number__icontains=unit_number)
        if is_occupied in {'true', 'false', '1', '0'}:
            qs = qs.filter(is_occupied=is_occupied in {'true', '1'})
        if tenant_id:
            qs = qs.filter(tenant_id=tenant_id)

        return qs

