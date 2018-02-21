from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from gds.api.views import SchedChangeAPIView, PassengerAPIView, ReservationAPIView

urlpatterns = [
    url( r'^schedchange/$', SchedChangeAPIView.as_view(), name='sched_chance' ),
    url( r'^passengers/$', PassengerAPIView.as_view(), name='list-passenger' ),
    url( r'^reservations/$', ReservationAPIView.as_view(), name='list-reservation' ),
]


