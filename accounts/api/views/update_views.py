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


class UpdatePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.request.user

        serializer = ChangePasswordSerializer(data = request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": "wrong_password"}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
