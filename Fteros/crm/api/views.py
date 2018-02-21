from django.db.models import Q
from rest_framework import generics, mixins, status
from crm.api.serializers import *
from crm.models import Affiliate, Customer, Contract, Markup, Reward, Dropnet, ExceptionAirline, User, UserManager, BugReport
from rest_framework.response import Response
from django.http import Http404

class AffiliateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = AffiliateSerializer

    def get_queryset(self):
        qs = Affiliate.objects.all()
        query = self.request.GET.get("name")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AffiliateRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = AffiliateSerializer

    def get_queryset(self):
        return Affiliate.objects.all()

class AirlineAPIView(generics.ListAPIView):
    serializer_class = AirlineSerializer

    def get_queryset(self):
        qs = Customer.objects.all().filter(
            Q(customer_type__iexact='V')
            ).distinct()
        return qs


class CustomerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = CustomerSerializer

    def get_queryset(self):
        qs = Customer.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains = query)|
                Q(interface_id__icontains = query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()

class ExceptionAirlineAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ExceptionAirlineSerializer

    def get_queryset(self):
        qs = ExceptionAirline.objects.all()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExceptionAirlineRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = ExceptionAirlineSerializer

    def get_queryset(self):
        return ExceptionAirline.objects.all()

class ContractAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        qs = Contract.objects.all() 
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains = query)|
                Q(description__icontains = query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContractRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        qs = Contract.objects.all()

        name = self.request.GET.get("name")
        
        if name is not None:
            qs = qs.filter(
                Q(contract__name__iexact = name)
                ).distinct()

        return qs



class MarkupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MarkupPostSerializer
        return MarkupReadSerializer

    def get_queryset(self):
        qs = Markup.objects.all() 
        
        # ------ Getting querystrings if exists ----------
        dk = self.request.GET.get("dk")
        
        if dk is not None:
            qs = qs.filter(
                Q(customer__interface_id__iexact = dk) 
                ).distinct()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MarkupRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = MarkupPostSerializer

    def get_queryset(self):
        return Markup.objects.all()

class RewardAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RewardPostSerializer
        return RewardReadSerializer

    def get_queryset(self):
        qs = Reward.objects.all() 
        
        # ------ Getting querystrings if exists ----------
        dk = self.request.GET.get("dk")
        
        if dk is not None:
            qs = qs.filter(
                Q(customer__interface_id__iexact = dk) 
                ).distinct()

        return qs
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RewardRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' 
    serializer_class = RewardPostSerializer

    def get_queryset(self):
        return Reward.objects.all

class DropnetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DropnetPostSerializer
        return DropnetReadSerializer

    def get_queryset(self):
        qs = Dropnet.objects.all() 
        airline = self.request.GET.get("airline")
        if airline is not None:
            qs = qs.filter(
                Q(airline__iexact = airline)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DropnetRudView(generics.RetrieveUpdateDestroyAPIView):
        lookup_field = 'id' 
        serializer_class = DropnetPostSerializer

        def get_queryset(self):
            return Dropnet.objects.all

class UserCreateAPIView(generics.CreateAPIView):

    model = User
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serialized = UserCreateSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UserListSerializer

    def get_queryset(self):
        qs = User.objects.all()
        query = self.request.GET.get("email")
        if query is not None:
            qs = qs.filter(
                Q(email__iexact=query)
                ).distinct()
        return qs


class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()


class TravelerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TravelerCreateSerializer
        return TravelerRudSerializer

    def get_queryset(self):
        qs = Traveler.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(first_name__icontains = query)|
                Q(last_name__icontains = query)|
                Q(traveler_of__interface_id__iexact = query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TravelerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = TravelerRudSerializer

    def get_queryset(self):
        return Traveler.objects.all()


class CommunicationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    
    serializer_class = CommunicationSerializer

    def get_queryset(self):
        qs = Communication.objects.all() # Getting all communication
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(agency__id__iexact=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommunicationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # slug, pk # url(r'?P<pk>\d+')
    serializer_class = CommunicationSerializer

    def get_queryset(self):
        return Communication.objects.all()

class BugReportAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = BugReportSerializer

    def get_queryset(self):
        qs = BugReport.objects.all()

        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BugReportAPIRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BugReportSerializer

    def get_queryset(self):
        return BugReport.objects.all()