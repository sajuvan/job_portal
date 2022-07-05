from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request,'employees/login.html')

def search_job(request):
    return render(request,'employees/home.html')

