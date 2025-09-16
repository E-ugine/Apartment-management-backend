from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLandlord, IsCaretaker, IsTenant


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsLandlord()]

class LandlordOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsLandlord]

    def get(self, request):
        return Response({"message": "Hello Landlord!"})


class CaretakerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCaretaker]

    def get(self, request):
        return Response({"message": "Hello Caretaker!"})


class TenantOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsTenant]

    def get(self, request):
        return Response({"message": "Hello Tenant!"})