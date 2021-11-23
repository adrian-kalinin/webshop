from django.urls import path

from . import views


app_name = 'shopping_cart'

urlpatterns = [
    path('get-items/', views.GetItemsView.as_view(), name='get-items'),
    path('add-item/', views.AddItemView.as_view(), name='add-item'),
    path('remove-item/', views.RemoveItemView.as_view(), name='remove-item')
]
