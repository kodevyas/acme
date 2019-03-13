import csv

from django.shortcuts import render
from django.views import View

from products.models import Product

# Create your views here.
class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'upload.html')

    def post(self, request):
        csv_file = request.FILES['file']
        content = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(content)
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
        return render(request, 'upload.html')
