import csv

from products.models import Product

from acme.celery import app as celery_app

@celery_app.task
def insert_records_to_db(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                product = Product.objects.get(sku=row['sku'])
                product.name = row['name']
                product.description = row['description']
                product.save()
            except Product.DoesNotExist:
                Product.objects.create(
                        sku=row['sku'],
                        name=row['name'],
                        description=row['description'])

