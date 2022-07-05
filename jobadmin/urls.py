
from django.urls import path
from . import views
app_name='jobadmin'

urlpatterns=[ 
     path('login',views.user_login,name='user'),
    path('view',views.view_emp,name='search'),  


]