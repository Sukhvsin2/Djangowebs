from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def home(request):
	products = Product.objects
	return render(request,'products/home.html',{'product':products})

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.POST['url'] and request.FILES['image']:
			# some code
			product = Product()
			product.title = request.POST['title']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']
			product.body = request.POST['body']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/products/' + str(product.id)) # what is product here ?

		else:
			return render(request,'products/create.html',{'Error':'Please fill all given fields.'})

	else:
		return render(request,'products/create.html')


def detail(request,product_id):
	product = get_object_or_404(Product,pk=product_id)
	return render(request,'products/details.html',{'product':product})

@login_required
def upvote(request,product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect('/products/' + str(product.id))