from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Login view placeholder")

def signup_view(request):
    return HttpResponse("Signup view placeholder")

def logout_view(request):
    return HttpResponse("Logout view placeholder")

def is_customer(user): return user.role == "customer"
def is_provider(user): return user.role == "provider"
def is_admin(user): return user.role == "admin"

@login_required
@user_passes_test(is_customer)
def customer_dashboard(request):
    return render(request, "dashboard/customer_dashboard.html")

@login_required
@user_passes_test(is_provider)
def provider_dashboard(request):
    return render(request, "dashboard/provider_dashboard.html")

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")

@login_required
@user_passes_test(is_customer)
def customer_shipments(request):
    return render(request, "dashboard/customer/shipments.html")

@login_required
@user_passes_test(is_customer)
def book_shipment(request):
    return render(request, "dashboard/customer/book_shipment.html")

@login_required
@user_passes_test(is_customer)
def track_shipment(request):
    return render(request, "dashboard/customer/track_shipment.html")

@login_required
@user_passes_test(is_customer)
def customer_payments(request):
    return render(request, "dashboard/customer/payments.html")

@login_required
@user_passes_test(is_provider)
def available_jobs(request):
    return render(request, "dashboard/provider/available_jobs.html")

@login_required
@user_passes_test(is_provider)
def my_assignments(request):
    return render(request, "dashboard/provider/assignments.html")

@login_required
@user_passes_test(is_provider)
def upload_pod(request):
    return render(request, "dashboard/provider/upload_pod.html")

@login_required
@user_passes_test(is_admin)
def analytics(request):
    return render(request, "dashboard/admin/analytics.html")

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    return render(request, "dashboard/admin/manage_users.html")

@login_required
@user_passes_test(is_admin)
def manage_shipments(request):
    return render(request, "dashboard/admin/manage_shipments.html")

@login_required
@user_passes_test(is_admin)
def settings_view(request):
    return render(request, "dashboard/admin/settings.html")

def index(request):
    return HttpResponse("Hello from core.views!")
