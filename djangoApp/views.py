from django.http import HttpResponse
from django.shortcuts import render



def check(request):
	return render(request, 'home.html')

