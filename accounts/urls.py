from django.urls import path
from django.shortcuts import redirect
from .views import signup, log_in, home, logout_view


def login_signup_redirect(request):
	return redirect('signup')


urlpatterns = [
	path('', home, name='home'),
	path('signup/', signup, name='signup'),
	path('login/', log_in, name='login'),
	path('login/signup', login_signup_redirect, name='login_signup_redirect'),
	path('logout/', logout_view, name='logout'),
	path('home/', home, name='home'),
]