import json
import uuid

import requests

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from core.models import ProductListing
from core.forms import PurchaseForm
from core import api_calls


class ProductListingView(generic.ListView):
    template_name = 'core/product_listing.html'
    context_object_name = 'product_listings'

    def get_queryset(self):
        return ProductListing.objects.all()


class ProductDetailView(generic.TemplateView):
    template_name = 'core/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs['product_id']
        context['product_detail'] = api_calls.fetch_product_detail(product_id)
        return context

class PurchaseView(generic.View):
    template_name = 'core/purchase_form.html'
    form_class = PurchaseForm

    def get(self, request, *args, **kwargs):
        product_id = kwargs['product_id']
        form =  self.form_class()
        return render(request, self.template_name, {
            'form': form,
            'product_id': product_id,
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        product_id = kwargs['product_id']
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        purchase = form.save(commit=False)
        if not api_calls.post_purchase(product_id, purchase):
            return HttpResponseRedirect('/failure/')
        product_detail = api_calls.fetch_product_detail(product_id)
        purchase.confirmation_code = uuid.uuid4()
        purchase.product_name = product_detail['name']
        purchase.product_price = product_detail['price']
        purchase.product_cost = product_detail['cost']
        purchase.product_cost = product_detail['cost']
        purchase.save()
        return HttpResponseRedirect('/success/')
