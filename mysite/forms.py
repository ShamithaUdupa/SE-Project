from django import forms

class LoginForm(forms.Form):
	username=forms.CharField(help_text="Enter your username",required=True)
	password=forms.CharField(widget=forms.PasswordInput)