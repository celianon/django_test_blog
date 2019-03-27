from django.urls import path, include

from .views import *

urlpatterns = [
	path('login/', Login.as_view(), name='login'),
	path('logout/', Logout.as_view(), name='logout'),
	path('register/', Register.as_view(), name='reg'),
]
