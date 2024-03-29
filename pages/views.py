from django.shortcuts import render

# Create your views here.from
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices

def index(request):
	listings = Listing.objects.all().filter(is_published=True)[:3] #maximum 3 listings

	context = {
	  'listings': listings,
	  'state_choices': state_choices,
	  'price_choices': price_choices,
	  'bedroom_choices': bedroom_choices

	}
	return render(request, 'pages/index.html', context)

def about(request):
	realtors = Realtor.objects.order_by('-hire_date')
	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
	context = {
		'realtors': realtors,
		'mvp_realtors': mvp_realtors
	}
	return render(request, 'pages/about.html', context)
