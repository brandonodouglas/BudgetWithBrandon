
from django import forms
import datetime
# https://docs.djangoproject.com/en/5.2/ref/forms/fields/

# Choices for the choice field
CATEGORY_CHOICES = (
    ("WANTS", "WANTS"),
    ("NEEDS", "NEEDS"),
    ("SAVINGS", "SAVINGS"),
    ("N/A","N/A"),
)

class TransactionForm(forms.Form):
    # Money in
    money_in = forms.IntegerField()
    # Money out
    money_out = forms.IntegerField()
    # current balance
    current_balance = forms.IntegerField()
    # payee - the person the user is paying e.g. landlord for rent
    payee = forms.CharField()
    # notes - optional notes concerning transaction e.g. UC PIP
    notes = forms.CharField()
    # dta -- Data stamp in DD/MM/YYYY format
    transaction_date = forms.DateField(initial=datetime.date.today)
    # Category - WANT, NEED, SAVINGS
    transaction_category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    # Type - Youtube subscription, week 1 groceries, obsidian subscription, rent payment (similar to ynab and its categorising)
    category_group = forms.CharField()