from rest_framework import serializers

from gds.models import SchedChange, Passenger, Reservation

class SchedChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedChange
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many = True, read_only = True)
    
    class Meta:
        model = Reservation
        fields = '__all__'

class SegmentSerializer(serializers.Serializer):
    name_file = serializers.CharField(max_length=50)