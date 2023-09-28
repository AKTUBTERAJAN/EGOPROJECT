from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','msg')
admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display= ('id','headlines','slider_dec','slider_picture')
admin.site.register(slider,sliderAdmin)

class volunteerAdmin(admin.ModelAdmin):
    list_display= ('id','name','email','mobile','city','current_position','picture')
admin.site.register(volunteer,volunteerAdmin)

class upcomingeventsAdmin(admin.ModelAdmin):
    list_display=('id','event_picture','event_title','event_details','event_date','event_place','event_purpose')
admin.site.register(upcomingevents,upcomingeventsAdmin)

class donateusAdmin(admin.ModelAdmin):
    list_display = ('id','name','picture','mobile','city','address','pincode','rupees','ddate')

admin.site.register(donateus,donateusAdmin)

class nhelpAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobile','helptype','message','address','picture','request_date')

admin.site.register(nhelp,nhelpAdmin)

class schangeAdmin(admin.ModelAdmin):
    list_display = ('id','title','picture','description')

admin.site.register(schange,schangeAdmin)