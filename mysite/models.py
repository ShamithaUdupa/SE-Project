from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
	title=models.CharField(max_length=50)
	isbn=models.IntegerField(primary_key=True)
	author=models.CharField(max_length=25)
	price=models.DecimalField(max_digits=7,decimal_places=2)
	quantity=models.IntegerField()
	image=models.ImageField(upload_to='books',default='books/book.jpg')
	
	def __str__(self):
		return self.title
		
class Shopping_Cart(models.Model):
	user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
	book=models.ManyToManyField(Book)
	
	def __str__(self):
		return str(self.user)
		
class Selling_Cart(models.Model):
	user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
	book=models.ManyToManyField(Book)
	
	def __str__(self):
		return str(self.user)
		
class Order(models.Model):
	orderid=models.AutoField(primary_key=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=1,null=True)
	book=models.ManyToManyField(Book)
	address=models.CharField(max_length=75)
	mobile=models.IntegerField()
	total=models.DecimalField(default=0,max_digits=7,decimal_places=2)
	paid=models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.orderid)
		
class Paid_Order(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	total=models.DecimalField(default=0,max_digits=7,decimal_places=2)
	
	def __str__(self):
		return str(self.user)

class Comment(models.Model):
	name=models.CharField(max_length=75)
	email=models.EmailField(max_length=75,null=True)
	message=models.CharField(max_length=300)

	def __str__(self):
		return str(self.message)

