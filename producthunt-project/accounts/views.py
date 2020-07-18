from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == 'POST':
		if request.POST['Password'] == request.POST['ConfirmPassword']:
			try:
				user = User.objects.get(username=request.POST['UserName'])
				return render(request,'accounts/signup.html',{'NameError':'Username is already taken!'})	
			except User.DoesNotExist:
				# Creating a new account
				user = User.objects.create_user(request.POST['UserName'],password = request.POST['Password'])
				auth.login(request,user)
				return redirect('home')

		else:
			return render(request,'accounts/signup.html',{'Error':'Password not matched.'})
	else:
		return render(request,'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['UserName'],password=request.POST['Password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')	
		else:
			return render(request,'accounts/login.html',{'Error':'Username or password is incorrect'})
	else:
		return render(request,'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')

