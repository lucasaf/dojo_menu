from django.shortcuts import render
from programa.models import Item

def index(request):

	items = Item.objects.all()

	return render(request,'index.html',{'items':items})

def adicionar(request):
	return render(request,'adicionar.html')
	

