from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from rest_framework import viewsets
from .serializers import TransactionSerializer
from .forms import TransactionForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# https://docs.djangoproject.com/en/5.2/topics/forms/#the-view
def get_transactions(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = TransactionForm()
    return render(request, "transactions.html", {"form": form})

class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

# Landing page
def home(request):
    return render(request, 'home.html')

# Called when user submits username and password in the view
# If username is not registered, throws appropiate error message
def login_page(request):
    # After form submission via POST request to here/server
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user exists from imported user
        if not User.objects.filter(username=username).exists():
            # Messsages --> send message to the user
            messages.error(request, 'The username submitted does not appear in the database')
            # Redirect back to the login page as user n
            return redirect('/login/')
        # Otherwise, authenticate the user via django authentication method
        # If user is no
        user = authenticate(username=username, password=password)
        # SUCCESS!
        if user is not None:
            # Here, the user is not none, "The "
            # Here, the userername and password is valid
            login(request, user)
            # Go to the homepage / landing page
            return redirect('/home/')
        # FAILURE
        else:
            messages.error(request, "The username and/or password is invalid")
            # Since the credentials are invalid, go back to the login page
            return redirect('/login/')
    # Not sure what this extra command does like isn't his the else of all other REST API Methods?
    return render(request, 'login.html')


            
    





        




    return render(request, 'login.html')


# Handles the register route
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check for registered user
        user = User.objects.filter(username=username)
        # If the user already exists in the datbase backend then a user with that username is already registered
        if user.exists():
            messages.info(request, "This username is already taken. Please choose another username.")
            # Go back to the register page
            return redirect('/register/')
        
        # If the username doesn't exist, register it into the backend
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    # Render the registration page template via get request
    return render(request,'register.html')
