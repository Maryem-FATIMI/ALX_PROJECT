E-Commerce API
Overview
This is an e-commerce API built with Django and Django Rest Framework (DRF) for managing products, categories, reviews, and wishlists. The project provides CRUD (Create, Read, Update, Delete) functionality for products and categories, as well as the ability for users to manage wishlists and leave reviews for products.

#################
Environment Setup:
 Install Django and Django REST Framework using pip, if not already installed: bash pip install django djangorestframework Create a new Django project named ecommerce_api: bash django-admin startproject ecommerce_api Navigate into your project directory and create a new Django app called "products" for order management and  : bash cd ecommerce_api python manage.py startapp products  , Add 'rest_framework', 'products'  to the INSTALLED_APPS in settings.py.
 ##################

 Features
Product Management:

CRUD operations for products (name, description, price, category, stock quantity, image, and creation date).
Products can be filtered by category and sorted by price, stock quantity, or creation date.
Ability to reduce stock quantity when an order is placed.
Category Management:

CRUD operations for categories.
Wishlist Management:

Users can add products to their wishlist.
Each user can only manage their own wishlist.
Review Management:

Users can leave reviews for products (rating and comments).
Reviews are filtered by product.
Authentication & Permissions:

Users must be authenticated to manage products, wishlists, and leave reviews.
Permissions are set to ensure that users can only manage their own data.
Requirements
Python 3.x
Django 3.x or higher
Django Rest Framework
Django Filter

##############

Endpoints
Authentication
POST /api/auth/login/ - Login a user and obtain an authentication token (for accessing protected endpoints).
Product Endpoints
GET /api/products/ - List all products.
GET /api/products/{id}/ - Retrieve details of a specific product by ID.
POST /api/products/ - Create a new product (requires authentication).
PUT /api/products/{id}/ - Update a product (requires authentication).
DELETE /api/products/{id}/ - Delete a product (requires authentication).
POST /api/products/{id}/reduce_stock/ - Reduce stock quantity for a product.
Category Endpoints
GET /api/categories/ - List all categories.
GET /api/categories/{id}/ - Retrieve details of a specific category by ID.
POST /api/categories/ - Create a new category (requires authentication).
PUT /api/categories/{id}/ - Update a category (requires authentication).
DELETE /api/categories/{id}/ - Delete a category (requires authentication).
Wishlist Endpoints
GET /api/wishlist/ - List products in the authenticated user's wishlist.
POST /api/wishlist/ - Add a product to the wishlist (requires authentication).
DELETE /api/wishlist/{id}/ - Remove a product from the wishlist (requires authentication).
Review Endpoints
GET /api/products/{product_id}/reviews/ - List all reviews for a specific product.
POST /api/products/{product_id}/reviews/ - Add a review for a product (requires authentication).