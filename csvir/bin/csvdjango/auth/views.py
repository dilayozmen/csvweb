from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
	context={}
	context.update(csrf(request))
	return render(request,'login.html',context)

def authenticate(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	#request.user.username gives username on page
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/auth/login')

def logout(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/auth/login/')
	username = request.user.username
	auth.logout(request)
	return HttpResponseRedirect('/home/')
