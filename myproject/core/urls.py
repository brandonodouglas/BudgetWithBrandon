
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
        # path("accounts/password_reset/", TemplateView.as_view(template_name="reset_password.html"), name="password_reset"),
          # path('accounts/password_reset/', views.PasswordResetView, name='password_reset'),

    # path('login/', views.login_view, name='login'),
    # path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('password_change', PasswordChangeView.as_view(template_name="users/password_change.html"), name="password_change"),
    # path('users/', include('django.contrib.auth.urls')),
    # 
    # path("sign_up/", views.sign_up, name = "sign_up"),
   # path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "password_reset.html"), name ='password_reset'),
  # path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
  # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
  # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete'),
      path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html")),
    path("", views.homepage, name="home"),
    path("about/", views.aboutpage, name="about"),
    path("accounts/", include("django.contrib.auth.urls")),




]