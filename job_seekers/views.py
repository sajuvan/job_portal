from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request,'job_seekers/login.html')

def search_job(request):
    return render(request,'job_seekers/jobsearch.html') 

def details_job(request):
    return render(request,'job_seekers/jobdetails.html')       
