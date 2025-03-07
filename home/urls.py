from django.urls import path 
from .import views 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("signout", views.signout, name="signout"),
    path("admin_index", views.admin_index, name="admin_index"),
    path("service_index", views.service_index, name="service_index"),
    path("merchant_index", views.merchant_index, name="merchant_index"),
    path("tax_mgt", views.tax_mgt, name="tax_mgt"),
    path("edit_tax/<int:pk>", views.edit_tax, name="edit_tax"),
    path("delete_tax/<int:pk>", views.delete_tax, name="delete_tax"),
    path("chat_user_list", views.chat_user_list, name="chat_user_list"),
    path("chat_view/<int:user_id>", views.chat_view, name="chat_view"),
    path("chat_with_user/<int:user_id>", views.chat_with_user, name="chat_with_user"),
    path("chat_list_merchant", views.chat_list_merchant, name="chat_list_merchant"),
    path("user_profile_update", views.user_profile_update, name="user_profile_update"),
    path("user", views.user, name="user"),
    path("user_update/<int:id>", views.user_update, name="user_update"),
    path("user_delete/<int:id>", views.user_delete, name="user_delete"),
    path("service_provider", views.service_provider, name="service_provider"),
    path("service_provider_update/<int:id>", views.service_provider_update, name="service_provider_update"),
    path("delete_service_provider/<int:id>", views.delete_service_provider, name="delete_service_provider"),
    path("add_service", views.add_service, name="add_service"),
    path("update_service/<int:service_id>", views.update_service, name="update_service"),
    path("delete_service/<int:service_id>", views.delete_service, name="delete_service"),
    path("book_service/<int:service_id>", views.book_service, name="book_service"),
    path("booking_list", views.booking_list, name="booking_list"),
    path("approve_booking/<int:booking_id>", views.approve_booking, name="approve_booking"),
    path("reject_booking/<int:booking_id>", views.reject_booking, name="reject_booking"),


    path("service_user", views.service_user, name="service_user"),
    path("myservice_booking", views.myservice_booking, name="myservice_booking"),
]


