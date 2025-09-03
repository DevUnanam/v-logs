from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def redirect_user(user):
    if user.role == "customer":
        return redirect("customer_dashboard")
    elif user.role == "provider":
        return redirect("provider_dashboard")
    elif user.role == "admin":
        return redirect("admin_dashboard")
    return redirect("login")

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_user(user)  # redirect after signup
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect_user(user)  # redirect after login
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
