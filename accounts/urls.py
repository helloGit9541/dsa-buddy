from django.urls import path,include
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_page,name='logout'),
    path('settings/',profile_settings,name='settings'),
]