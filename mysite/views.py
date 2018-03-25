from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Shopping_Cart,Selling_Cart,Order,Paid_Order,Comment
from django.contrib.auth.models import User,Group
from django import template
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as authlogout
regis=template.Library()
# Create your views here.

@regis.simple_tag
def add(a,b):
	return a+b

@regis.filter(name='has_group')
def has_group(user,group_name):
	group=Group.objects.get(name=group_name)
	return group in user.groups.all()

def index(request):
	result=Book.objects.all()
	message=request.GET.get('message')
	if message is not None:
		Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
	return render(request,'index.html',{'context':result})
	
	
def user(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		if username!="":
			user=authenticate(username=username,password=password)
			print(request.user.get_username())
			if user is not None and user.is_active:
				login(request,user)
				if user.groups.filter(name='Clerks').exists():
					result=Order.objects.all()
					return render(request,'manager.html',{'context':result})
				elif user.groups.filter(name='Customers').exists():
					result=Book.objects.all()
					return render(request,'index.html',{'context':result})
			else:
				return render(request,'registration/login.html')
		else:
			return render(request,'registration/login.html')
	elif request.method == 'GET':
		query=request.GET.get('query')
		if query is None:
			user=request.user
			if user.groups.filter(name='Clerks').exists():
				result=Order.objects.all()
				return render(request,'manager.html',{'context':result})
			else:
				result=Book.objects.all()
				message=request.GET.get('message')
				if message is not None:
					Comment.objects.create(name=request.user.get_username(),email=request.user.email,message=message)
		else:
			if request.user is not None and request.user.groups.filter(name='Clerks').exists():
				result=Order.objects.filter(address=query)
				return render(request,'manager.html',{'context':result})
			else:
				result=Book.objects.filter(title=query)
		return render(request,'index.html',{'context':result})

def contact(request):
	return render(request,'contact.html')
	
def signup(request):
	return render(request,'register.html')

def register(request):
	if request.method == 'POST':
		username=request.POST.get('username',request.user.get_username())
		password=request.POST.get('password')
		email=request.POST.get('email')
		reset=request.POST.get('reset','default')
		if reset=="default":
			if User.objects.filter(username=username).count()==0 and password!="" and email!="" and username!="":
				obj=User.objects.create_user(username=username,password=password,email=email)
				my_group = Group.objects.get(name='Customers') 
				my_group.user_set.add(obj)
			else:
				return render(request,'register.html')
		else:
			obj=User.objects.get(username=username)
			obj.set_password(password)
			obj.email=email
			obj.save()
		# print(request.user.get_username())
		return render(request,'registration/login.html')
	message=request.GET.get('message')
	if message is not None:
		Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
	return render(request,'register.html')
		
def shoppingcart(request):
	if request.method == 'GET':
		var=request.GET.get('action','')
		if(var=="add"):
			b1=Book.objects.get(isbn=request.GET.get('isbn'))
			u1=User.objects.get(username=request.user.get_username())
			count=Shopping_Cart.objects.filter(user=u1).count()
			if count==1:
				s1=Shopping_Cart.objects.get(user=u1)
			else:
				s1=Shopping_Cart.objects.create(user=u1)
			s1.book.add(b1)
		elif(var=="remove"):
			s=Shopping_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			b1=Book.objects.get(isbn=request.GET.get('isbn'))
			s.book.remove(b1)
		message=request.GET.get('message')
		if message is not None:
			Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
		try:
			s=Shopping_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			obj=s.book.all()
		except Shopping_Cart.DoesNotExist:
			obj=None
		return render(request,'shoppingcart.html',{'context':obj})
	
def sellingcart(request):
	if request.method == 'GET':
		var=request.GET.get('action','')
		if(var=="remove"):
			s=Selling_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			b1=Book.objects.get(isbn=request.GET.get('isbn'))
			s.book.remove(b1)
			b1.delete()
		message=request.GET.get('message')
		if message is not None:
			Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
		try:
			s=Selling_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			obj=s.book.all()
		except Selling_Cart.DoesNotExist:
			obj=None
		return render(request,'sellingcart.html',{'context':obj})
	elif request.method == 'POST':
		var=request.POST.get('action','')
		if(var=="add") and request.POST.get('title')!="" and request.POST.get('price')!="" and request.POST.get('quantity')!="":
			b1=Book.objects.create(isbn=request.POST.get('isbn'),title=request.POST.get('title'),author=request.POST.get('author'),price=request.POST.get('price'),quantity=request.POST.get('quantity'),image=request.FILES['image'])
			u1=User.objects.get(username=request.user.get_username())
			count=Selling_Cart.objects.filter(user=u1).count()
			if count==1:
				s1=Selling_Cart.objects.get(user=u1)
			else:
				s1=Selling_Cart.objects.create(user=u1)
			s1.book.add(b1)
		try:
			s=Selling_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			obj=s.book.all()
		except Selling_Cart.DoesNotExist:
			obj=None
		return render(request,'sellingcart.html',{'context':obj})

def profile(request):
	username=request.user.get_username()
	obj=User.objects.get(username=username)
	message=request.GET.get('message')
	review=request.GET.get('review')
	if message is not None:
		Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
	if review is not None:
		Comment.objects.create(name=request.user.get_username(),email=request.user.email,message=review)
	try:
		s=Paid_Order.objects.filter(user=User.objects.get(username=request.user.get_username()))
		o=Order.objects.filter(user=User.objects.get(username=request.user.get_username()))
	except Paid_Order.DoesNotExist:
		s=None
	except Order.DoesNotExist:
		o=None
	return render(request,'profile.html',{'context':obj,'transactions':s,'orders':o})

def order(request):
	if request.method == 'GET':
		var=request.GET.get('action','')
		message=request.GET.get('message')
		if message is not None:
			Comment.objects.create(name=request.GET.get('name'),email=request.GET.get('email'),message=message)
		if var == "pay":
			o=Order.objects.get(orderid=request.GET.get('orderid'))
			Paid_Order.objects.create(user=o.user,total=o.total)
			o.delete()
			result=Order.objects.all()
			return render(request,'manager.html',{'context':result})
		else:
			s=Shopping_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
			s.save()
			obj=s.book.all()
			bill=0
			for j in obj:
				bill=bill+j.price
			return render(request,'order.html',{'context':obj,'total':bill})
	elif request.method == 'POST':
		s=Shopping_Cart.objects.get(user=User.objects.get(username=request.user.get_username()))
		s.save()
		obj=s.book.all()
		bill=0
		for j in obj:
			bill=bill+j.price
			j.quantity=j.quantity-1
			j.save()
		o=Order.objects.create(address=request.POST.get('address'),mobile=request.POST.get('mobile'),user=User.objects.get(username=request.user.get_username()),total=bill)
		for j in obj:
			o.book.add(j)
		return render(request,'shoppingcart.html',{'context':obj})
	
def logout(request):
	authlogout(request)
	result=Book.objects.all()
	return render(request,'index.html',{'context':result})
