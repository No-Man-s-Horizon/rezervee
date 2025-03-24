from django.urls import path
from django.views.decorators.cache import cache_page
from reservations.api.views import (
    ReservationListAPIView,
    ReservationDetailAPIView,
    ReservationDeleteAPIView,
    ReservationUpdateAPIView,
    ReservationCreateAPIView,
    )


app_name = 'reservations'


urlpatterns = [
    path('list', cache_page(60 * 1)(ReservationListAPIView.as_view()), name='list'),
    path('detail/<pk>', ReservationDetailAPIView.as_view(), name='detail'),
    path('update/<pk>', ReservationUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>', ReservationDeleteAPIView.as_view(), name='delete'),
    path('create', ReservationCreateAPIView.as_view(), name='create'),
]
