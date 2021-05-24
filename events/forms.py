from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class EventForm(ModelForm):
	class Meta:
		model = event
		fields = '__all__'
		exclude = ['count','customer','cancel_event','count2']
		widgets= {
            'Event_Date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Event_Time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
			'description':forms.Textarea
        }

class DeletForm(ModelForm):
	class Meta:
		model = event
		fields = ['cancel_event']
		
		
		
		

		
class EventRegisterForm(ModelForm):
	class Meta:
		model = register
		fields = '__all__'
		exclude = ['status','count']
		widgets={'customer':forms.HiddenInput,'event_name':forms.HiddenInput}

class ConfirmForm(ModelForm):
	class Meta:
		model = register
		fields = ['status']
		
class UpdateRegisterForm(ModelForm):
	class Meta:
		model = register
		fields = '__all__'
		exclude = ['customer','event_name','status','count']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

