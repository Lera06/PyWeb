import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from store.models import Product, Category


if __name__=="__main__":
    category = Category.objects.get(name='Vegetables')
    obj = Product(name='Chilli', description='Chilli', price=120,
                  image='static/products/product-12.jpg',
                  category=category)
    obj.save()







