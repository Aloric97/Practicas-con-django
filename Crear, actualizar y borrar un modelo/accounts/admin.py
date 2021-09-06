from django.contrib import admin
from .models import *


admin.site.register(costumer)

admin.site.register(product)
admin.site.register(order)

admin.site.register(tag)