from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Transaction
import datetime




# https://docs.djangoproject.com/en/5.2/ref/forms/fields/
# User registration form data (with email)
# https://dev.to/donesrom/how-to-set-up-django-built-in-registration-in-2023-41hg
# https://www.youtube.com/watch?v=AZYTPI_YXNM&list=PLaUQIPIyD0z43DiRKM0x8YNEB-1QNCOwR&index=6
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["email"]


class RegistrationForm(UserCreationForm):
    # additional fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    # Always include a meta class
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class PSWDForm(PasswordResetForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["email",]


# Choices for the choice field
CATEGORY_CHOICES = (
    ("WANTS", "WANTS"),
    ("NEEDS", "NEEDS"),
    ("SAVINGS", "SAVINGS"),
    ("N/A","N/A"),
)




 # This form is similar to the transaction models code
class TransactionForm(forms.ModelForm):
    MONTHS = {
    1: ("jan"),
    2: ("feb"),
    3: ("mar"),
    4: ("apr"),
    5: ("may"),
    6: ("jun"),
    7: ("jul"),
    8: ("aug"),
    9: ("sep"),
    10: ("oct"),
    11: ("nov"),
    12: ("dec"),
}
    YEARS = { 
    1999:("1999"),
    2000:("2000"),
    2001:("2001"),
    2002:("2002"),
    2003:("2003"),
    2004:("2004"),
    2005:("2005"),
    2006:("2006"),
    2007:("2007"),
    2008:("2008"),
    2009:("2009"),
    2010:("2010"),
    2011:("2011"),
    2012:("2012"),
    2013:("2013"),
    2014:("2014"),
    2015:("2015"),
    2016:('2016'),
    2017:("2017"),
    2018:("2018"),
    2019:("2019"),
    2020:("2020"),
    2021:("2021"),
    2022:("2022"),
    2023:("2023"),
    2024:("2024"),
    2025:("2025"),
    2026:("2026"),
    2027:("2027"),
    2028:("2028"),
    2029:("2029"),
    2030:("2030"),
    2031:("2031"),
    2032:("2032"),
    2033:("2033"),
    2034:("2034"),
    2035:("2035"),
    }
    
    transaction_date = forms.DateField(
        widget=forms.SelectDateWidget(months=MONTHS, years=YEARS)
    )
    class Meta:
        model = Transaction
        fields = ['money_in', 'money_out', 'current_balance', 'category', 'transaction_date','tag', 'payee', 'account', 'description', 'cleared']
    
        
# Timeline formt
