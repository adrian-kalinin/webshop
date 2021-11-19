from django.urls import path

from . import views


app_name = 'catalogue'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<product_code>/', views.ProductDetailView.as_view(), name='detail')
]
