from django.urls import path

from . import views


app_name = 'shopping_cart'

urlpatterns = [
    path('get/', views.GetItemsView.as_view(), name='get-items'),
    path('add/', views.AddItemView.as_view(), name='add-item'),
    path('remove/', views.RemoveItemView.as_view(), name='remove-item')
]
