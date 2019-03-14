from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
from django.db.models import Q
from django.views import View

from .models import Product

# Create your views here.

class ListProductsView(View):

    def get(self, request):

        # Taking out expected query parameters

        query = request.GET.get('query', '')
        active = request.GET.get('active', None)
        page = request.GET.get('page', 1)

        # creating a query with ORM + filtering with OR using Q

        all_products = Product.objects.filter(
                Q(sku__icontains=query) | Q(name__icontains=query)).order_by('name')

        # if active parameter is present then add one more filter
        if active:
            is_active = bool(int(active))
            all_products = all_products.filter(active__exact=is_active)

        # Do pagination
        paginator = Paginator(all_products, 20)

        # get the required page from paginator
        products = paginator.get_page(page)
        context = {
                'inactive_filter_url': request.GET.urlencode() + '&active=0',
                'active_filter_url': request.GET.urlencode() + '&active=1', 
                'products': products
                }
        return render(request, 'products.html', context)

class DeleteAllProducts(View):

    def post(self, request):

        products = Product.objects.all().delete()
        return redirect('upload')
