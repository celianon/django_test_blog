from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class LoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class': 'form-control',
		'autofocus': '',
		}))

	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class': 'form-control',
		}))

	def clean(self):
		cleaned_data = super().clean()
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			
			if not user:
				raise ValidationError('Username or password is incorrect!')
			if not user.is_active:
				raise ValidationError('user is not active!')

class RegForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		widgets = {
			'username' : forms.TextInput(attrs={'class': 'form-control','autofocus': '' }),
			'email' : forms.EmailInput(attrs={'class': 'form-control'}),
			'password' : forms.PasswordInput(attrs={'class': 'form-control'})
		}

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		email = cleaned_data.get('email1')
		password = cleaned_data.get('password')

		if User.objects.filter(email=email):
			raise ValidationError('User with this email already exist!')
		if len(password) < 6:
			raise ValidationError('Password most be longer then 6!')