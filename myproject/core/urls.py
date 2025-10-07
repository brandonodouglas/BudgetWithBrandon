
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

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html")),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("accounts/password_reset/done/", views.passwordresetdonepage, name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("accounts/reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("", views.homepage , name="home"),
    path('admin/', admin.site.urls),
    path("about/", views.aboutpage, name="about"),
    path("accounts/register/", views.registerpage, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]