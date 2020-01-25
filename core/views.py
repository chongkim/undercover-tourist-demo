import json

import requests

from django.shortcuts import render
from django.views import generic

from core.models import ProductListing


class ProductListingView(generic.ListView):
    template_name = 'core/product_listing.html'
    context_object_name = 'product_listings'

    def get_queryset(self):
        return ProductListing.objects.all()


class ProductDetailView(generic.TemplateView):
    template_name = 'core/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs['id']
        response = requests.get(f'https://careers.undercovertourist.com/assignment/1/products/{product_id}', headers={
            'X-Auth': 'chong.kim',
        })
        # this is assuming that the status is ok
        context['product_detail'] = json.loads(response.text)
        return context
