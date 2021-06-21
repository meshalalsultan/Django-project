from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,"index.html")

def real(request):
	return render(request,"real.html")	


