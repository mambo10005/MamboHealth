from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm  # or your custom form

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            # Authenticate with username and password
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            if user is not None:
                login(request, user)  # This now works properly
                return redirect("/")  # or your desired redirect
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
