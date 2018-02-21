from django.contrib import admin

from . models import SchedChange, Passenger, Travel, Reservation

admin.site.register(SchedChange)
admin.site.register(Passenger)
admin.site.register(Reservation)
admin.site.register(Travel)
