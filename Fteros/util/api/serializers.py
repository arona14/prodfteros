from rest_framework import serializers
from util.models import ConnectionSetting

class ConnectionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionSetting
        fields = '__all__'
