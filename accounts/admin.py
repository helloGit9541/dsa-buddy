from django.contrib import admin

# Register your models here.
from accounts.models import *

admin.site.register(DsaUser)
admin.site.register(Topic)
admin.site.register(Problem)