# import forms and USerCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
#impoort model
from django.contrib.auth.models import User

#create class y hereda la UserCreationForm


class CustomRegisterForm(UserCreationForm):
	#inside this you will have already all fields, username, passwd1 and 2
	# add email field

	# create an instance and use form que heredaste

	email = forms.EmailField()
	# email tiene parametro que by default es required. si no ponemos nada es requiered. si queremos que sea opcional ponerr
	# forms.EmailField(required=False)


	# use meta to configure everything related to forrm
	# configure your model: on which model, on which db and table content should be  saved

	class Meta:
		model = User
		# fields must be in order
		fields = ['username', 'email', 'password1', 'password2']