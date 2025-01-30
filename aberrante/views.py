from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead
from .forms import SimpleForm

def home(request):

	if request.method == 'POST':
		form = SimpleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	
	else:
		form = SimpleForm()

	leads = Lead.objects.all()

	return render(request, 'home.html', {'form': form, 'leads': leads})
