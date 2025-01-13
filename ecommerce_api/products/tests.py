from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from products.models import Product, Category

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        # Create test categories
        self.category1 = Category.objects.create(name="Electronics")
        self.category2 = Category.objects.create(name="Clothing")

        # Create test products
        Product.objects.create(
            name="Smartphone",
            description="Latest smartphone.",
            price=599.99,
            category=self.category1,
            stock_quantity=10,
            image_url="http://example.com/smartphone.jpg"
        )
        Product.objects.create(
            name="Laptop",
            description="High-performance laptop.",
            price=999.99,
            category=self.category1,
            stock_quantity=5,
            image_url="http://example.com/laptop.jpg"
        )
        Product.objects.create(
            name="T-Shirt",
            description="Comfortable cotton t-shirt.",
            price=19.99,
            category=self.category2,
            stock_quantity=100,
            image_url="http://example.com/tshirt.jpg"
        )

    def test_product_list_pagination(self):
        # Test pagination for product listing
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertLessEqual(len(response.data["results"]), 10)  # Assuming default page size is 10

    def test_product_search(self):
        # Test search functionality for product names
        response = self.client.get("/api/products/?search=Smartphone")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Smartphone")

    def test_filter_by_category(self):
        # Test filtering by category
        response = self.client.get(f"/api/products/?category={self.category1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)  # Electronics category has 2 products

    def test_filter_by_price_range(self):
        # Test filtering by price range
        response = self.client.get("/api/products/?min_price=500&max_price=1000")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)  # Products in the 500-1000 range

    def test_filter_by_stock_availability(self):
        # Test filtering by stock availability
        response = self.client.get("/api/products/?in_stock=True")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)  # All products have stock > 0
