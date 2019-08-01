from django.urls import path

from . import views

urlpatterns = [
    path("", views.shopping, name="shopping"),
    path("buy/<str:category>/<str:name>/<int:pk>", views.buy_view, name="buy"),
    path("cart", views.cart_view, name="cart"),
    path("orders/<str:username>", views.orders_view, name="orders"),
    path("/orders/delete/<str:username>", views.delete_order, name="delete_order"),
    path("/orders/manage/<str:username>", views.manage_orders_view, name="manage_orders"),

]
