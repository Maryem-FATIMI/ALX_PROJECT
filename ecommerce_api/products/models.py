"""Product Management (CRUD):

Implement the ability to Create, Read, Update, and Delete (CRUD) products.
Each product should have the following attributes: Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date.
Ensure validation for required fields like Price, Name, and Stock Quantity.
Make sure the Stock Quantity is automatically reduced when an order is placed (future enhancement or consider as optional for now).
Users Management (CRUD):

Implement CRUD operations for users who will manage the products.
A user should have a unique Username, Email, and Password.
Only authenticated users should be able to manage products (i.e., create, update, delete)."""
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock_quantity = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    