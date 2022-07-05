from django.urls import URLPattern, path
from . import views
urlpatterns=[
    
    path('login',views.user_login,name='user'),
    path('home',views.search_job,name='search'), 


]