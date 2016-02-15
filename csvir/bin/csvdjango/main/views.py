from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
import subprocess
import os

# Create your views here.
def home(request):
	return render(request,"home.html")
