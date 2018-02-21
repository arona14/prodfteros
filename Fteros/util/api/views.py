from django.db.models import Q
from rest_framework import generics, mixins
from util.api.serializers import ConnectionSettingSerializer
from util.models import ConnectionSetting



class ConnectionSettingAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'name'
    serializer_class = ConnectionSettingSerializer
    

    def get_queryset(self):
        qs = ConnectionSetting.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__iexact = query)
                ).distinct()
        return qs



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConnectionSettingRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name' 
    serializer_class = ConnectionSettingSerializer

    def get_queryset(self):
        return ConnectionSetting.objects.all()
