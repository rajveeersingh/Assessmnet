from django.urls import path
from .views import *
urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('register',Register.as_view(),name='register'),
    path('detail',Detail.as_view(),name='detail'),
    path('logout',Logout.as_view(),name='logout'),
    path('newticket',NewTickets.as_view(),name='ticket'),
    
]


