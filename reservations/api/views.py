from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.mixins import DestroyModelMixin
from accounts.api.throttles import RegisterThrottle
from reservations.api.paginations import ReservationPagination
from reservations.api.permissions import IsOwner
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser
)
from reservations.models import Reservation
from .serializers import ReservationSerializer, ReservationUpdateCreateSerializer


class ReservationListAPIView(ListAPIView):
    # throttle_scope  = 'domain'
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # permission_classes = [IsAuthenticated]
    # filter_backends = [SearchFilter, OrderingFilter]
    #search_fields = ['full_name','description'] # api/v1/reservations/list?search=must&ordering=full_name
    pagination_class = ReservationPagination

    # def get_queryset(self):
    #     queryset = Reservation.objects.filter(draft=False)
    #     return queryset


class ReservationDetailAPIView(RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk' #pk or slug


class ReservationDeleteAPIView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class ReservationUpdateAPIView(RetrieveUpdateAPIView):  # UpdateAPIView
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    # def perform_update(self, serializer):
    #     serializer.save(modified_by = self.request.user)


class ReservationUpdateWithDeleteAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        queryset = Reservation.objects.filter(
            vendor=serializer.validated_data['vendor'],
            datetime=serializer.validated_data['datetime'])
        if queryset.exists():
            raise ValidationError('The vendor has already been registered')
        serializer.save(user = self.request.user)
