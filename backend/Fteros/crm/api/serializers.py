from rest_framework import serializers
from django.contrib.auth.models import Group
from crm.models import *

class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = [
            'id',
            'name'
            ]



class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'interface_id'
            ]

class ExceptionAirlineSerializer(serializers.ModelSerializer):
    aircode = serializers.ReadOnlyField(source = 'airline.interface_id')
    class Meta:
        model = ExceptionAirline
        fields = [
            'id',
            'airline',
            'contract',
            'aircode',
            'net_value',
            'pub_value',
            'com_value'
            ]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class MarkupReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)
    x_airlines = ExceptionAirlineSerializer(source="exceptionairline_set", many = True, read_only = True)

    class Meta:
        model = Markup
        fields = '__all__'


class MarkupPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Markup
        fields = '__all__'

class RewardReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)

    class Meta:
        model = Reward
        fields = '__all__'

class RewardPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'

class DropnetReadSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only = True)

    class Meta:
        model = Dropnet
        fields = '__all__'
class DropnetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dropnet
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'customer',
            'role',
            'gds',
            'sign',
            'agent_cc'
            ]

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name'
            ]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    role = RoleSerializer( read_only = True)
    customer = CustomerSerializer(read_only = True)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'role',
            'customer',
            'gds',
            'sign',
            'agent_cc'
            ]

class TravelerRudSerializer(serializers.ModelSerializer):
    traveler_of = CustomerSerializer(read_only = True)

    class Meta:
        model = Traveler
        fields = '__all__'


class TravelerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traveler
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = '__all__'

class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugReport
        fields = '__all__'

