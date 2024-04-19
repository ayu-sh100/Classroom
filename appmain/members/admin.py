from django.contrib import admin
from .models import CustomUser,Role,Organization
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(Organization)

