from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm  # or your custom form

from health_data.models import HealthRecord, HealthViewPreference
from django.utils.dateformat import format as date_format

from django.contrib.auth.decorators import login_required
from health_data.utils import get_field_labels
from django.core.serializers.json import DjangoJSONEncoder
import json

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

