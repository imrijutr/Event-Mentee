from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(event)
admin.site.register(Tag)
admin.site.register(register)

