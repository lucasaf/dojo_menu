from django.shortcuts import render, HttpResponseRedirect
from programa.models import Item

def index(request):

	items = Item.objects.all()

	return render(request,'index.html',{'items':items})

def adicionar(request):
	return render(request,'adicionar.html')

def salvar(request):
	if request.method ==  'POST':
		codigo = request.POST.get('codigo','0')

		try:
			item = Item.objects.get(pk=codigo)
		except: 
			item = Item()
		
		item.nome = request.POST.get('nome')
		item.valor = request.POST.get('valor')
		item.save()
	return HttpResponseRedirect('/')

def editar(request, pk=0):

	item = Item.objects.get(pk=pk)
	
	return render(request, 'adicionar.html', {'item':item})



