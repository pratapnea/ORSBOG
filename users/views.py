from django.shortcuts import render

# Create your views here.
def index(request):
	companiesList={
		'companies': [
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.',
					'Mastergogo Pvt. Ltd.'
					],
	}
	return render(request, "users/index.html", companiesList)

def login(request):
	return render(request, "users/login.html")

def signup_user(request):
	return render(request, "users/register.html")

def signup_company(request):
	return render(request, "users/register.html")

def logout(request):
	print("logout")