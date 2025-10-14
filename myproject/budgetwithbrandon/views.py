from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from rest_framework import generics
from .serializers import TransactionSerializer, TimelineSerializer
from .forms import PSWDForm, RegistrationForm, TransactionForm, CustomPasswordResetForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import *
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet




            
# Serialization
class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TimelineViewSext(ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    
    





# Landing page
def homepage(request):
    return render(request, "home.html")

# About page
def aboutpage(request):
    return render(request, "about.html")

# Register view - working 
def registerpage(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})

# Password reset done view
def passwordresetdonepage(request):
    return render(request, "password_reset_done.html")


def PasswordResetSuccessView(request):
    return render(request, "password_reset_success.html")
# forgot your password view, i.e. password reset
def forgotpasswordpage(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to password reset done page
            return redirect(passwordresetdonepage)
    else:
        form = CustomPasswordResetForm()
    return render(request, "password_reset.html", {"form": form})

# Login views



            
    




        







