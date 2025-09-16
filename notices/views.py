from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Notice
from .serializers import NoticeSerializer
from users.permissions import IsLandlord, IsLandlordOrCaretaker


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.select_related('recipient', 'created_by').all()
    serializer_class = NoticeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        # Only landlord or caretaker can create/update/delete notices
        return [permissions.IsAuthenticated(), IsLandlordOrCaretaker()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        role = getattr(user, 'role', None)

        # Tenants should see tenant-targeted or their own notices; caretakers/landlords see all
        if role == 'tenant':
            qs = qs.filter(Q(audience='all') | Q(audience='tenants') | Q(recipient=user))

        # Simple filters
        audience = self.request.query_params.get('audience')
        created_by = self.request.query_params.get('created_by')
        recipient = self.request.query_params.get('recipient')

        if audience:
            qs = qs.filter(audience=audience)
        if created_by:
            qs = qs.filter(created_by_id=created_by)
        if recipient:
            qs = qs.filter(recipient_id=recipient)

        return qs

