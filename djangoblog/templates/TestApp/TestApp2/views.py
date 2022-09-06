from django.shortcuts import render

def Login(request):
    return render(request,'home.html')

def Data(request):
    return render(request,'index.html')