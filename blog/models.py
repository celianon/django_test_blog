from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

from pytils.translit import slugify

def gen_slug(title):
	slug = slugify(title)
	return slug + '_' + str(int(time()))


class Post(models.Model):
	author = models.CharField(db_index=True, max_length=150, default='admin')
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	body = models.TextField(max_length=8000 ,blank=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	tag = models.ManyToManyField('Tag', blank=True, related_name='posts')

	def get_absolute_url(self):
		return reverse('post_detail_url', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def get_update_url(self):
		return reverse('post_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('post_delete_url', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=50, db_index=True)
	slug = models.SlugField(max_length=50,blank=True, unique=True)
	author = models.CharField(max_length=150, default='anonamuse')

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tags_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('tag_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('tag_delete_url', kwargs={'slug': self.slug})
