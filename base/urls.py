from django.urls import include,path
from base.views import *

app_name = 'base'

urlpatterns = [
    path('',home,name="home"),
]