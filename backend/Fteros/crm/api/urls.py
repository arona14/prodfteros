from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

from crm.api.views import *

urlpatterns = [
    url(r'^account/token/$', obtain_jwt_token),
    url(r'^account/user/create/$', UserCreateAPIView.as_view(), name='user-create' ),
    url(r'^account/users/$', UserListAPIView.as_view(), name='user-list' ),
    url(r'^account/users/(?P<id>\d+)/$', UserRudView.as_view(), name='user-rud' ),
    url(r'^affiliates/$', AffiliateAPIView.as_view(), name='affiliate-create' ),
    url(r'^affiliates/(?P<id>\d+)/$', AffiliateRudView.as_view(), name='affiliate-rud' ),
    url( r'^customers/$', CustomerAPIView.as_view(), name='customer-create' ),
    url( r'^customers/(?P<id>\d+)/$', CustomerRudView.as_view(), name='customer-rud' ),
    url(r'^airlines/$', AirlineAPIView.as_view(), name='airline-list' ),
    url( r'^airlinexceptions/$', ExceptionAirlineAPIView.as_view(), name='exception-create' ),
    url(r'^airlinexceptions/(?P<id>\d+)/$', ExceptionAirlineRudView.as_view(), name='airline-exeption-rud' ),
    url(r'^contracts/$', ContractAPIView.as_view(), name='contract-create' ),
    url(r'^contracts/(?P<id>\d+)/$', ContractRudView.as_view(), name='contract-rud' ),
    url(r'^markups/$', MarkupAPIView.as_view(), name='markup-list' ),
    url(r'^markups/(?P<id>\d+)/$', MarkupRudView.as_view(), name='markup-rud' ),
    url(r'^rewards/$', RewardAPIView.as_view(), name='reward-list' ),
    url(r'^rewards/(?P<id>\d+)/$', RewardRudView.as_view(), name='reward-rud' ),
    url(r'^dropnets/$', DropnetAPIView.as_view(), name='dropnet-list' ),
    url(r'^dropnets/(?P<id>\d+)/$', DropnetRudView.as_view(), name='dronet-rud' ),
    url(r'^travelers/$', TravelerAPIView.as_view(), name='traveler-create' ),
    url(r'^travelers/(?P<id>\d+)/$', TravelerRudView.as_view(), name='traveler-rud' ),
    url(r'^communications/$', CommunicationAPIView.as_view(), name='communication-create' ),
    url(r'^communications/(?P<id>\d+)/$', CommunicationRudView.as_view(), name='traveler-rud' ),
    url( r'^bugreport/$', BugReportAPIView.as_view(), name='create-bug' ),
    url(r'^bugreport/(?P<id>\d+)/$', BugReportAPIRudView.as_view(), name='bug-rud' )
]


