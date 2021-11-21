from django.urls import path

from . import views


app_name = 'catalogue'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('<product_code>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<product_code>/edit', views.ProductUpdateView.as_view(), name='product-update'),
    path('<product_code>/delete', views.ProductDeleteView.as_view(), name='product-delete')
]
