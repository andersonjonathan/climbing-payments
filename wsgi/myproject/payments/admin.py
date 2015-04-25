from django.contrib import admin

# Register your models here.
from .models import *


class PassengerInLine(admin.TabularInline):
    model = Passenger
    extra = 4


class TravelAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['where', "driver"]}),
        ('Date information', {'fields': ['when']}),
    ]
    inlines = [PassengerInLine]
    list_per_page = 50


#admin.site.register(Question)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Place)
admin.site.register(Person)
admin.site.register(Passenger)
admin.site.register(MyTrip)