from django.urls import path
from . import views
app_name='job_seekers'
urlpatterns=[
    path('login',views.user_login,name='user'),
    path('jobsearch',views.search_job,name='search'), 
    path('jobdetails',views.details_job,name='job'),
]

