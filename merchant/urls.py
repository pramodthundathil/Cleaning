from django.urls import path 
from .import views 

urlpatterns = [
    path("merchants_admin",views.merchants_admin,name="merchants_admin"),
    path("delete_merchant/<int:pk>",views.delete_merchant,name="delete_merchant"),
    path("edit_merchant/<int:pk>",views.edit_merchant,name="edit_merchant"),
    path("products_merchant",views.products_merchant,name="products_merchant"),
    path("edit_product/<int:pk>",views.edit_product,name="edit_product"),
    path("category",views.category,name="category"),
    path("add_images/<int:pk>",views.add_images,name="add_images"),
    path("cart",views.cart,name="cart"),
    path("add_to_cart/<int:pk>",views.add_to_cart,name="add_to_cart"),
    path("delete_cart_item/<int:pk>",views.delete_cart_item, name="delete_cart_item"),
    path("update_cart",views.update_cart,name="update_cart"),
    path("delete_category/<int:pk>", views.delete_category, name="delete_category"),


    path("order_creation",views.order_creation,name="order_creation"),
    path("Payment_screen/<int:pk>",views.Payment_screen,name="Payment_screen"),
    path("add_to_order/<int:item_id>",views.add_to_order,name="add_to_order"),
    path("callback/", views.callback, name="callback"),
    path("orders",views.orders,name="orders"),
    path("orders_merchant",views.orders_merchant,name="orders_merchant"),
    path("Generate_invoice/<int:pk>",views.Generate_invoice,name="Generate_invoice"),
    path("chat",views.chat,name="chat"),

    path("products",views.products,name="products"),
    path("product_details/<int:pk>",views.product_details,name="product_details"),
    path("add_review/<int:pk>",views.add_review, name="add_review"),


    path("view_single_order/<int:pk>",views.view_single_order,name="view_single_order"),
    # path("order_status_update/<int:pk>",views.order_status_update,name="order_status_update"),
    path("update_order_status/<int:order_id>/<str:status>", views.update_order_status, name="update_order_status"),
    path("promotions_offers",views.promotions_offers,name="promotions_offers"),
    path("Add_merchant_promotions",views.Add_merchant_promotions,name="Add_merchant_promotions"),
    path("delete_promotion/<int:pk>", views.delete_promotion, name="delete_promotion"),
]