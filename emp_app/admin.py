from django.contrib import admin
from .models import *

# Register your models here.
# username=tony
# password=tony123
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)