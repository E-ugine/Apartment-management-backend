from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer
from users.permissions import IsLandlordOrCaretaker


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('tenant', 'unit').all()
    serializer_class = PaymentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        # Create/update/delete payments allowed for landlords and caretakers
        return [permissions.IsAuthenticated(), IsLandlordOrCaretaker()]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        role = getattr(user, 'role', None)

        # Scope by role
        if role == 'tenant':
            qs = qs.filter(tenant=user)

        # Simple filters
        unit_id = self.request.query_params.get('unit_id')
        status = self.request.query_params.get('status')
        method = self.request.query_params.get('method')
        tenant_id = self.request.query_params.get('tenant_id')

        if unit_id:
            qs = qs.filter(unit_id=unit_id)
        if status:
            qs = qs.filter(status=status)
        if method:
            qs = qs.filter(method=method)
        if tenant_id:
            qs = qs.filter(tenant_id=tenant_id)

        return qs

