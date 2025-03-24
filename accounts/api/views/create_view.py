from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from accounts.api.permissions import NotAuthenticated
from accounts.api.serializers import RegisterSerializer
from accounts.api.throttles import RegisterThrottle


class CreateUserView(CreateAPIView):
    # throttle_classes = [RegisterThrottle]
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]
