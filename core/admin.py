from django.contrib import admin
from core.models import Visitor,Practitioner, User
admin.site.register(User)
admin.site.register(Visitor)
admin.site.register(Practitioner)