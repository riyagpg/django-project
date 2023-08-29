from django.contrib import admin
# from app1.models import Userregister,Category,Product,Order
from app1.models import *
# Register your models here.


class userdisplay(admin.ModelAdmin):
    list_display=['name','email','number']
    list_filter=['name','number']
    search_fields=['name']
admin.site.register(Userregister,userdisplay)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)



class contactdisplay(admin.ModelAdmin):
    list_display=['name','email','message']
    list_filter=['name','number']
    search_fields=['name']
admin.site.register(Contactus,contactdisplay)