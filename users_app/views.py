from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.


def register(request):
	# Check if this is a POST REQUEST. If so, take request, save it to db check form validation 
	# if request is GET, display register page

	if request.method == 'POST':
		# create an instance from you CustomRegisterForm
		# since this is post, request will have somekind of content, request.POST
		register_form = CustomRegisterForm(request.POST)
		#Check if yourr formr is valid
		if register_form.is_valid():
			# If its valid, save form, handle message and add redirect
			register_form.save()
			messages.success(request, ('New user has been created'))
			return redirect('register')

	else:
		register_form = CustomRegisterForm()
	return render(request, 'register.html', {'register_form': register_form})