from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request,'jobadmin/login.html')

def view_emp(request):
    return render(request,'jobadmin/view employees.html')
