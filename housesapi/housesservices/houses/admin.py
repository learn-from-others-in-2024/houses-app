from django.contrib import admin

from .models import House
from .models import Checker


# Register your models here.
admin.site.register(House)
admin.site.register(Checker)
