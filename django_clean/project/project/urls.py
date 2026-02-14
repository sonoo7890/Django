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
from .import views
from .views import landing,register,login,dashboard,add_emp,add_dep
from django.conf import settings
from django.conf.urls.static import static
# from app.views import login, register
# from app.views import dashboard, admin_dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('register/',views.register, name='register'),
    # path('registerdata/', registerdata, name='registerdata'),
    path('show_data/',views.show_data,name="show_data"),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/add_emp/',views.add_emp,name='add_emp'),
    path('dashboard/add_dep/',views.add_dep,name='add_dep'),
    path('dashboard/all_dep/',views.all_dep,name='all_dep'),
    path('dashboard/all_emp/',views.all_emp,name='all_emp'),
    path('show_query/',views.show_query,name='show_query'),
    path('dashboard/profile/',views.profile,name='profile'),
    path('dashboard/query',views.query,name='query'),
    path('dashboard/query_status',views.query_status,name='query_status'),
    path('dashboard/all_query',views.all_query,name='all_query'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('query_data/',views.query_data,name='query_data'),
    path('reply_query/<int:pk>',views.reply_query,name='reply_query'),
    path('userdashboard/query/edit/<int:pk>/',views.edit,name='edit'),
    path('userdashboard/query/update/<int:pk>/',views.update,name='update'),
    # path('userdashboard/delete_query/<int:pk>/',delete_query, name='delete_query'),
    path('reset/',views.reset,name='reset'),



    path('delete/<int:pk>',views.delete,name='delete'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)