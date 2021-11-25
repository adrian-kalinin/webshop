from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q

from .models import Product
from .forms import ProductModelForm


class ProductListView(generic.ListView):
    template_name = 'catalogue/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()

        if query := self.request.GET.get('q'):
            queryset = queryset.filter(Q(title__contains=query) | Q(product_code__exact=query))

        sort_value = self.request.GET.get('sort') or '-created_at'

        return queryset.order_by(sort_value)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super(ProductListView, self).get_context_data(**kwargs)
        context_data['search_value'] = self.request.GET.get('q')
        context_data['sort_value'] = self.request.GET.get('sort')
        return context_data


class ProductDetailView(generic.DetailView):
    template_name = 'catalogue/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_code = self.kwargs.get('product_code')
        return Product.objects.get(product_code=product_code)


class ProductCreateView(PermissionRequiredMixin, generic.CreateView):
    template_name = 'catalogue/product_create.html'
    form_class = ProductModelForm
    permission_required = 'catalogue.add_product'

    def get_success_url(self):
        return reverse('catalogue:list')


class ProductUpdateView(PermissionRequiredMixin, generic.UpdateView):
    template_name = 'catalogue/product_update.html'
    form_class = ProductModelForm
    permission_required = 'catalogue.change_product'

    def get_object(self, queryset=None):
        pc = self.kwargs.get('product_code')
        return Product.objects.filter(product_code=pc).first()

    def get_success_url(self):
        return reverse('catalogue:product-detail', kwargs={'product_code': self.kwargs.get('product_code')})


class ProductDeleteView(PermissionRequiredMixin, generic.DeleteView):
    template_name = 'catalogue/product_delete.html'
    permission_required = 'catalogue.delete_product'

    def get_object(self, queryset=None):
        pc = self.kwargs.get('product_code')
        return Product.objects.filter(product_code=pc).first()

    def get_success_url(self):
        return reverse('catalogue:list')
