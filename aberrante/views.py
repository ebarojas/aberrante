from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lead
from .forms import SimpleForm, LeadTypeForm
from django.conf import settings

def home(request):
	if request.method == 'POST':
		simple_form = SimpleForm()
		lead_form = LeadTypeForm()

		if "lead_form" in request.POST:
			lead_form = LeadTypeForm(request.POST)
			if lead_form.is_valid():
				lead_form.save()
				return redirect('home')
		elif "simple_form" in request.POST:
			simple_form = SimpleForm(request.POST)
			if simple_form.is_valid():
				simple_form.save()
				return redirect('home')
	else:
		simple_form = SimpleForm()
		lead_form = LeadTypeForm()

	leads = Lead.objects.all()

	return render(request, 'home.html', {'lead_form': lead_form, 'simple_form': simple_form, 'leads': leads, "MEDIA_URL": settings.MEDIA_URL})
