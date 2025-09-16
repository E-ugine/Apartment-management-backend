from rest_framework import viewsets, permissions
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer
from users.permissions import IsLandlord, IsCaretaker, IsTenant, IsLandlordOrCaretaker


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.select_related('unit', 'created_by', 'assigned_to').all()
    serializer_class = MaintenanceRequestSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        # Tenants can create requests; landlords/caretakers can update/delete
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsTenant()]
        return [permissions.IsAuthenticated(), IsLandlordOrCaretaker()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        role = getattr(user, 'role', None)

        # Tenants see only their own created requests; caretakers/landlords see all
        if role == 'tenant':
            qs = qs.filter(created_by=user)

        # Simple filters
        unit_id = self.request.query_params.get('unit_id')
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        assigned_to = self.request.query_params.get('assigned_to')

        if unit_id:
            qs = qs.filter(unit_id=unit_id)
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        if assigned_to:
            qs = qs.filter(assigned_to_id=assigned_to)

        return qs

