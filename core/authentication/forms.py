from django import forms

class TransactionForm(forms.Form):
    # Money in
    # Money out
    # current balance
    # payee - the person the user is paying e.g. landlord for rent
    # notes - optional notes concerning transaction e.g. UC PIP
    # dta -- Data stamp in DD/MM/YYYY format
    # Category - WANT, NEED, SAVINGS
    # Type - Youtube subscription, week 1 groceries, obsidian subscription, rent payment (similar to ynab and its categorising)
