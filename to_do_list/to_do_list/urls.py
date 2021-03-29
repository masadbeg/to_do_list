"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from user.views import UserView
from category.views import CategoryView
from task.views import TaskView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    path('user/<int:pk>',UserView.as_view({'get':'retrieve', 'put': 'update', 'delete':'destroy'})), 
    path('category/<int:pk>', CategoryView.as_view({'get':'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('category/create', CategoryView.as_view({'post':'create'})),
    path('user', UserView.as_view({'get':'list'})),
    path('task', TaskView.as_view({'get':'list',})),
    path('task/create', TaskView.as_view({'post':'create'})),
    path('task/<int:pk>', TaskView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),



]
