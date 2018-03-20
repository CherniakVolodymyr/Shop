from django.contrib import admin
from .models import *
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
        # display all in obg by field.obg
    list_filter = ('name',)# filter by name ("obg", )
    #exclude = ["email"] # all obg exclude field by ["obg"]
    #fields = ["email"] # show only obg in [obg, ... , ...]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)