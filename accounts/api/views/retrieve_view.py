from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.permissions import NotAuthenticated
from accounts.api.serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer
from accounts.api.throttles import RegisterThrottle


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id = self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
