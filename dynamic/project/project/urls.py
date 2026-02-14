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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

from app.views import login,register
import app.views as views

from app.views import dashboard, admin_dashboard,add_employee
from app.views import add_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing', landing, name='landing'),
    path('register/', register, name='register'),
    # path('registerdata/', registerdata, name='registerdata'),
    path('show_data/', show_data, name='show_data'),
    path('dashboard/',dashboard,name='dashboard'),
    path('',login,name='login'),
    path('login/',login, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/',logout,name='logout'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('show-employee/', views.show_employee, name='show_employee'),
     path("add-employee/", views.add_employee, name="add_employee"),
    path("show-employee/", views.show_employee, name="show_employee"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
