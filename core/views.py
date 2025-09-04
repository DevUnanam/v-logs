from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import random, string
from dashboard.models import Shipment
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

def generate_tracking_number():
    return "TRK" + "".join(random.choices(string.digits, k=7))

@login_required
def book_shipment(request):
    if request.method == "POST":
        shipment = Shipment.objects.create(
            customer=request.user,
            pickup_address=request.POST["pickup_address"],
            pickup_city=request.POST["pickup_city"],
            pickup_state=request.POST["pickup_state"],
            dropoff_address=request.POST["dropoff_address"],
            dropoff_city=request.POST["dropoff_city"],
            dropoff_state=request.POST["dropoff_state"],
            package_description=request.POST["package_description"],
            weight=request.POST["weight"],
            dimensions=request.POST["dimensions"],
            price=100.00,  # for now, static price
            tracking_number=generate_tracking_number(),
        )
        return redirect("track_shipment")

    return render(request, "dashboard/customer/book_shipment.html")

def track_shipment(request):
    shipment = None
    if request.method == "POST":
        tracking_number = request.POST.get("tracking_number")
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number, customer=request.user)
        except Shipment.DoesNotExist:
            shipment = None
            error = "No shipment found with this tracking number."
            return render(request, "dashboard/customer/track_shipment.html", {"error": error})

    return render(request, "dashboard/customer/track_shipment.html", {"shipment": shipment})
