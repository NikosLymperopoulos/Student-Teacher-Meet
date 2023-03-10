from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
# Create your views here.


def register(response):
    if response.user.is_authenticated:  # Den exei nohma oi logged in users na vlepoun to view afto
        return redirect("/")

    if response.method == "POST":
        page_data = response.POST
        form = RegisterForm(page_data)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login_user(response):
    if response.user.is_authenticated:  # Den exei nohma oi logged in users na vlepoun to log in view
        return redirect("/")

    if response.method == "POST":
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect("/")
        else:
            return redirect("login_user")
    else:
        return render(response, "authenticate/login.html", {})


def logout_user(response):
    if not response.user.is_authenticated:  # Den exei nohma oi mh logged in users na kanoun log out
        return redirect("/")

    logout(response)
    return redirect("login_user")


def loggedin(response):
    return render(response, "register/logged_in.html", {})