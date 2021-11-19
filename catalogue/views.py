from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    template_name = 'catalogue/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = 'catalogue/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_code = self.kwargs.get('product_code')
        return Product.objects.get(product_code=product_code)
