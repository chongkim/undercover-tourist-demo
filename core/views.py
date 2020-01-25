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
