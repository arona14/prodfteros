from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
from util.api.views import ConnectionSettingAPIView, ConnectionSettingRudView

urlpatterns = [
    url( r'^connection/setting/$', ConnectionSettingAPIView.as_view(), name='connection-setting-create' ),
    url(r'^connection/setting/(?P<name>[a-z]+)/$', ConnectionSettingRudView.as_view(), name='connection-setting-rud' ),
]
