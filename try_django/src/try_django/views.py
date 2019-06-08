from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import ContactForm

def home_view(request):
	title = "Hello there.. "
	if request.user.is_authenticated:
		title = "Hello, {}".format(request.user)
	return render(request, "hello_world.html", {'title': title})

def about_view(request):
	title = "About Us"
	return render(request, "about.html", {'title': title})

def contact_view(request):
	title = "Contact Us"
	
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		# re-initialized the form so that it should not hold previous value after submission
		form = ContactForm()
	else:
		print("Form validation failed!")

	context = {
		'title': title,
		'form' : form
	}

	return render(request, "form.html", context)
	#return JsonResponse("{'one': 1, 'two': 2}", safe=False)