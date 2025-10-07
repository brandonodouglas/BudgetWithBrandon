
from django.contrib import admin  # Django admin module
from django.urls import path, include       # URL routing
from budgetwithbrandon.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from rest_framework import routers
from budgetwithbrandon import views
from django.views.generic.base import TemplateView  # new
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    LogoutView,
)





router = routers.DefaultRouter()# https://www.pythontutorial.net/django-tutorial/django-password-reset/


# For help on the success_url see: https://stackoverflow.com/questions/52905645/django-password-reset-done-page-overriding-my-custom-url
urlpatterns = [
    path("accounts/password_change/", auth_views.PasswordChangeView.as_view(template_name="password_change.html"),name="password_change"),
    # !! PASSWORD RESET PATHS !!
    # Allows a user to reset their password by generating a one-time use link that can be used to reset the password, and sending that link to the user’s registered email address.
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html", success_url="success/"), name="password_reset"),
    # The page shown after a user has been emailed a link to reset their password. This view is called by default if the PasswordResetView doesn’t have an explicit success_url URL set.
    path("accounts/password_reset/done", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done"), name="password_reset_done"),
    # url For when the user has successfully reset their password
    path("accounts/password_reset/success/", views.PasswordResetSuccessView, name="password_reset_success"),
    # Simole django login supplied with a template
    path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html")),
    # Allows the user to reset their password by sending one-time use link and is also used to send the link to a designated email address
    # Provides a form for entering a new password
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    # Provides a view which informs the user that the password has been successfully change
    path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("", views.homepage , name="home"),
    path('admin/', admin.site.urls),
    path("about/", views.aboutpage, name="about"),
    path("accounts/register/", views.registerpage, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]