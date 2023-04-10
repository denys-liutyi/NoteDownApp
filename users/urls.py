"""Define regular expressions for Users App"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    #Add the default URL AUTH (authentification)
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]