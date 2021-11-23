from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
import json

from catalogue.models import Product
from .models import Cart


class AddItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data = json.loads(data)

        if product_id := data.get('product_id'):
            cart = Cart.objects.get(user_id=request.user.id)
            items = cart.items.all()

            if item := items.filter(product_id=product_id).first():
                item.quantity += 1
                item.save()
            else:
                product = Product.objects.get(id=product_id)
                cart.items.create(product=product, quantity=1)

            return HttpResponse()

        return HttpResponseBadRequest()


class RemoveItemView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        data = json.loads(data)

        if product_id := data.get('product_id'):
            cart = Cart.objects.get(user_id=request.user.id)
            items = cart.items.all()

            if item := items.filter(product_id=product_id).first():
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()

                else:
                    item.delete()

            return HttpResponse()

        return HttpResponseBadRequest()


class GetItemsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user_id=request.user.id)
        items = cart.items.all()

        # A serializer from DRF should be used here, but I didn't want to make things complicated here
        data = {'items': []}

        for item in items:
            data['items'].append({
                'product_id': item.product.id,
                'quantity': item.quantity,
                'title': item.product.title,
                'price': item.product.price,
                'image': item.product.image.url
            })

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder))
