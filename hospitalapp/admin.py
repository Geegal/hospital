from django.contrib import admin
from hospitalapp.models import Users, Product, Member, Message, Appointment, ImageModel

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Appointment)
admin.site.register(ImageModel)
