import csv

from django.shortcuts import render
from django.views import View
from django.core.files.storage import default_storage

from products.models import Product

from .tasks import insert_records_to_db

# Create your views here.
class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'upload.html')

    def post(self, request):
        csv_file = request.FILES['file']
        file_name = default_storage.save(csv_file.name, csv_file)
        insert_records_to_db.delay(file_name)
        return render(request, 'upload.html')
