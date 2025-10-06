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




            

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")

            
    else:
        form = RegistrationForm()
    return render(request, "sign_up.html", {"form": form})
    
    

# https://docs.djangoproject.com/en/5.2/topics/forms/#the-view
class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TimelineListCreate(generics.ListCreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

class TimelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer





# Landing page
def homepage(request):
    return render(request, "home.html")

# About page
def aboutpage(request):
    return render(request, "about.html")

# Register view
def registerpage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})
            
    




        







