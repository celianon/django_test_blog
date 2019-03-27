from django.shortcuts import render, redirect
from django.views.generic import View
from .form import LoginForm, RegForm
from django.contrib.auth import authenticate, login, logout


class Login(View):

	def get(self, request):
		login_form = LoginForm()
		return render(request, 'accounts/login.html', context={'form': login_form})

	def post(self, request):
		next = request.GET.get('next')
		bound_form = LoginForm(request.POST or None)
		if bound_form.is_valid():
			username = bound_form.cleaned_data.get('username')
			password = bound_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			login(request, user)

			if next:
				return redirect(next)
			else:	
				return redirect('/')

		for error in bound_form.errors:
			errors = bound_form.errors.get(error)

		return render(request, 'accounts/login.html', context={'form':bound_form, 'errors': errors})


class Logout(View):

	def get(self, request):
		next = request.GET.get('next')
		logout(request)

		if next:
			return redirect(next)

		return redirect('/')


class Register(View):

	def get(self, request):
		form = RegForm()
		return render(request, 'accounts/reg.html', context={'form': form})

	def post(self, request):
		bound_form = RegForm(request.POST)
		next = request.GET.get('next')

		if bound_form.is_valid():
			user = bound_form.save(commit=False)
			password = bound_form.cleaned_data.get('password')
			email = bound_form.cleaned_data.get('email')
			user.set_password(password)
			user.email = email
			user.save()
			new_user = authenticate(username=user.username, password=password)
			login(request, new_user)

			if next:
				return redirect(next)
			return redirect('/')

		for error in bound_form.errors:
			errors = bound_form.errors.get(error)

		return render(request, 'accounts/reg.html', context={'form': bound_form, 'errors': errors})
