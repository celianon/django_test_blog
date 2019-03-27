from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.shortcuts import HttpResponse

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectDeleteMixin
from .form import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator


def main(request):
	search = request.GET.get('search', '')
	if search:
		posts = Post.objects.filter(title__icontains=search).order_by('-date_pub')
		
	else:
		posts = Post.objects.all().order_by('-date_pub')

	page_num = request.GET.get('page', 1)
	paginate = Paginator(posts, 5)
	page = paginate.get_page(page_num)

	return render(request, 'blog/blog_base.html', context={'posts' : page, 'search':search})


def tag_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags' : tags})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tags_details.html'

	
class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = TagForm
	template = 'blog/tag_create.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = PostForm
	template = 'blog/post_create.html'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'blog/post_delete.html'
	redirect_url = 'posts_list_url'
	raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'blog/tag_delete.html'
	redirect_url = 'tags_list_url'
	raise_exception = True


class TagUpdate(LoginRequiredMixin, View):
	raise_exception = True

	def get(self, request, slug):
		tag = Tag.objects.get(slug__iexact=slug)
		bound_form = TagForm(instance=tag)
		if request.user.username == tag.author or request.user.is_staff:
			return render(request, 'blog/tag_update.html', context={'tag': tag, 'form': bound_form})
		else:
			raise PermissionDenied

	
	def post(self, request, slug):
		tag = Tag.objects.get(slug__iexact=slug)
		bound_form = TagForm(request.POST, instance=tag)

		if bound_form.is_valid():
			new_obj = bound_form.save(commit=True)
			return redirect(new_obj)
		return render(request, 'blog/tag_update.html', context={'tag': tag, 'form': bound_form})


class PostUpdate(LoginRequiredMixin, ObjectDetailMixin, View):
	raise_exception = True
	
	def get(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		bound_form = PostForm(instance=post)
		if request.user.username == post.author or request.user.is_staff:
			return render(request, 'blog/post_update.html', context={'post':post, 'form': bound_form})
		else:
			raise PermissionDenied

	def post(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		bound_form = PostForm(request.POST, instance=post)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render(request, 'blog/post_update.html', context={'post':post, 'form': bound_form})
