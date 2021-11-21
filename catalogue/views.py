from django.shortcuts import reverse
from django.views import generic

from .models import Product
from .forms import ProductModelForm


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


class ProductCreateView(generic.CreateView):
    template_name = 'catalogue/product_create.html'
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse('catalogue:list')


class ProductUpdateView(generic.UpdateView):
    template_name = 'catalogue/product_update.html'
    form_class = ProductModelForm

    def get_object(self, queryset=None):
        pc = self.kwargs.get('product_code')
        return Product.objects.filter(product_code=pc).first()

    def get_success_url(self):
        return reverse('catalogue:product-detail', kwargs={'product_code': self.kwargs.get('product_code')})


class ProductDeleteView(generic.DeleteView):
    template_name = 'catalogue/product_delete.html'

    def get_object(self, queryset=None):
        pc = self.kwargs.get('product_code')
        return Product.objects.filter(product_code=pc).first()

    def get_success_url(self):
        return reverse('catalogue:list')
