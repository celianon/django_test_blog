from django.shortcuts import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.exceptions import PermissionDenied

from .models import Post, Tag

class ObjectDetailMixin:

	model = None
	template = None

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		return render(request, self.template, context={
			self.model.__name__.lower():obj, 'admin_obj': obj, 'admin_panel_check':True 
			})


class ObjectCreateMixin:

	form_model = None
	template = None

	def get(self, request):
		form = self.form_model
		return render(request, self.template, context={'form': form})

	def post(self, request):
		user = request.user.username
		bound_form = self.form_model(request.POST)
		
		if bound_form.is_valid():

			new_obj = bound_form.save(commit=False)
			new_obj.author = user
			new_obj.save()
			bound_form.save_m2m() 
			
			return redirect(new_obj)
		return render(request, self.template, context={'form': bound_form})

class ObjectDeleteMixin:
	model = None
	template = None
	redirect_url = None

	def get(self, request, slug):

		obj = self.model.objects.get(slug__iexact=slug)
		if request.user.username == obj.author or request.user.is_staff:
			return render(request, self.template, context={self.model.__name__.lower(): obj,
														   'not_sidebar': True})
		else:
			raise PermissionDenied
	def post(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		obj.delete()
		return redirect(reverse(self.redirect_url))
