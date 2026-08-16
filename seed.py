
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')
django.setup()

from store.models import Product

if Product.objects.count() == 0:
    Product.objects.create(name="Wireless Headphones", price=99.99, description="High quality sound headphones.", image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400")
    Product.objects.create(name="Smart Watch", price=149.50, description="Track your daily activity and health.", image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
    Product.objects.create(name="Gaming Mouse", price=49.99, description="Ergonomic RGB optical gaming mouse.", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400")
