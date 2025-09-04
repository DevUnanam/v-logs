"""
URL configuration for vlogs_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views  # ✅ now correctly imports from core/views.py

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),

    # Dashboards
    path("dashboard/customer/", views.customer_dashboard, name="customer_dashboard"),
    path("dashboard/provider/", views.provider_dashboard, name="provider_dashboard"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),

    # Customer features
    path("shipments/", views.customer_shipments, name="customer_shipments"),
    path("shipments/book/", views.book_shipment, name="book_shipment"),
    path("shipments/track/", views.track_shipment, name="track_shipment"),
    path("payments/", views.customer_payments, name="customer_payments"),

    # Provider features
    path("jobs/", views.available_jobs, name="available_jobs"),
    path("assignments/", views.my_assignments, name="my_assignments"),
    path("upload-pod/", views.upload_pod, name="upload_pod"),

    # Admin features
    path("analytics/", views.analytics, name="analytics"),
    path("users/", views.manage_users, name="manage_users"),
    path("shipments/manage/", views.manage_shipments, name="manage_shipments"),
    path("settings/", views.settings_view, name="settings"),

    # Include other apps' URLs
    path("users/", include("users.urls")),      # If users app has urls.py
    path("dashboard/", include("dashboard.urls")),  # If dashboard app has urls.py
]

