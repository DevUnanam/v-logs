from django.urls import path
from . import views

urlpatterns = [
    path("customer/", views.customer_dashboard, name="customer_dashboard"),
    path("provider/", views.provider_dashboard, name="provider_dashboard"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
]
