from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from users.models import User


@login_required
@role_required(allowed_roles=['customer'])
def customer_dashboard(request):
    return render(request, "dashboard/customer_dashboard.html")

@login_required
@role_required(allowed_roles=['provider'])
def provider_dashboard(request):
    return render(request, "dashboard/provider_dashboard.html")

@login_required
@role_required(allowed_roles=['admin'])
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")
