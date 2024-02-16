from django.urls import path
from myapp import views
from . import views
urlpatterns=[path('',views.Home),path('About',views.About),path('Service',views.Service),path('Setting',views.Setting),path('Resume',views.Resume),path('secondpage',views.secondpage),path('Contact',views.Contact)]
