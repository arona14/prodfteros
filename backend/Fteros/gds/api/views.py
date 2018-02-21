from django.db.models import Q
from rest_framework import generics, mixins
from gds.api.serializers import SchedChangeSerializer, PassengerSerializer, ReservationSerializer
from gds.models import SchedChange, Passenger, Reservation


# this view allow only read methods
class SchedChangeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = SchedChangeSerializer

    def get_queryset(self):
        qs = SchedChange.objects.all() # Getting all contracts
        
        # ------ Getting querystrings if exists ----------
        dk = self.request.GET.get("dk")
        
        if dk is not None:
            qs = qs.filter(
                Q(dk = dk) # searching for contracts with agency_id
                ).distinct()

        return qs


    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)


class PassengerAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return Passenger.objects.all()


class ReservationAPIView(generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        qs = Reservation.objects.all()

        dk = self.request.GET.get("dk")
        if dk is not None:
            qs = qs.filter(
                Q(interface_id = dk)
                ).distinct()

        return qs