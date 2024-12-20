from django.urls import path
from .views import *
app_name='project'
urlpatterns=[
    path('main',main,name='main'),
    path('',home,name='home'),
    path('course',course,name='course'),
    path('bootcamp',Bootcamp,name='bootcamp'),
    path('request',RequestCallBack,name='request'),
    path('signin',sign,name='signin'),
]