from django import forms
from django.core.exceptions import ValidationError
from .models import Tag
from .models import Post

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['title']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'})
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['title'].lower()
		if new_slug == 'create':
			raise ValidationError('Slug can not be "create"')
		while Tag.objects.filter(slug__iexact=new_slug).count():
			new_slug = new_slug + '1'
		return new_slug


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title','body', 'tag']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}


	# def clean_slug(self):
