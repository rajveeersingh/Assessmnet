from django.urls import path
from .views import register,login,logout,newTickets,detail
urlpatterns = [
    path('',login.as_view(),name='login'),
    path('register',register.as_view(),name='register'),
    path('detail',detail.as_view(),name='detail'),
    path('logout',logout.as_view(),name='logout'),
    path('newticket',newTickets.as_view(),name='ticket'),
    
]


