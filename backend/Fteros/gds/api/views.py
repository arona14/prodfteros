from django.db.models import Q
from rest_framework import generics, mixins
from gds.api.serializers import SchedChangeSerializer, PassengerSerializer, ReservationSerializer,SegmentSerializer
from gds.models import SchedChange, Passenger, Reservation
from gds.request.detail import Segment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


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

class SegmentView(APIView):

    def get(self, request, format=None):

        file_name = request.query_params.get('name_file', None)
        if file_name is not None:
            resul = Segment().get_segment(file_name)
        else:
            #raise exceptions.ValidationError({'file_name': [_('This field is required')]})
            resul = 'This field is required'
        return Response(resul)
