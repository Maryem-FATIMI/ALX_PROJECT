from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')

        # Create a superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created'))

        # Create categories
        categories = [
            'Electronics',
            'Books',
            'Clothing',
            'Home & Garden'
        ]

        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)
            self.stdout.write(self.style.SUCCESS(f'Category "{cat_name}" created'))

        # Create products
        products = [
            ('Smartphone', 'Latest model smartphone', 999.99, 'Electronics', 50),
            ('Python Cookbook', 'Recipes for mastering Python', 39.99, 'Books', 100),
            ('T-shirt', 'Comfortable cotton t-shirt', 19.99, 'Clothing', 200),
            ('Plant Pot', 'Ceramic pot for indoor plants', 24.99, 'Home & Garden', 75)
        ]

        admin_user = User.objects.get(username='admin')

        for name, description, price, category, stock in products:
            category = Category.objects.get(name=category)
            Product.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'price': price,
                    'category': category,
                    'stock_quantity': stock,
                    'image_url': 'https://example.com/placeholder.jpg',  # placeholder image URL
                    'user': admin_user  # Set the user field
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Product "{name}" created'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))