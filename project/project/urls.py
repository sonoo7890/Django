"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing,name='landing'),
<<<<<<< HEAD
    path('set/',set,name='set'),
    path('set_data/',set_data,name='set_data'),
    path('get_data/',get_data,name='get_data'),
    path('delete_data/',delete_data,name='delete_data'),

=======
    path('my_home/',my_home,name='my_home'),
    path('my_about/',my_about,name='my_about'),
    path('my_contact/',my_contact,name='my_contact'),
    path('my_services/',my_services,name='my_services'),
    path('my_registration/',my_registration,name='my_registration'),
    path('my_login/',my_login,name='my_login'),
>>>>>>> fdc7b92f5dfacec0c5d5d482cb38ef15f9c80442
]
