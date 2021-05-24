"""eventclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from events import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    path('account/', views.accountSettings, name="account"),

    path('index/', views.index, name='index'),

    path('Create_Event/<str:pk>/', views.events, name='Create_Event'),
    path('Confirm_Participation/<str:pk>/', views.confirm, name='confirm'),
    path('Event_details/<str:pk>/', views.Event_details, name='Event_details'),
    path('All_Upcoming_Event',views.All_Upcoming_Event, name='All_Upcoming_Event'),
    path('All_registered_Event',views.All_registered_Event, name='All_registered_Event'),


    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('Register/<str:pk>/', views.RegisterEvent, name="RegisterEvent"),
    path('update_details/<str:pk>/', views.updateRegister, name="update_details"),
    path('update_event/<str:pk>/', views.updateEvent, name="update_event"),
    path('delete_event/<str:pk>/', views.deleteEvent, name="delete_event"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
