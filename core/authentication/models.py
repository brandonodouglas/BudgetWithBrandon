from django.db import models
from django.contrib.auth.models import User



# Choie for the tag field
TAG_CHOICES = [
    ("--", "--"),
    ("INCOME", "INCOME"),
    ("WANTS", "WANTS"),
               ("NEEDS", "NEEDS"),
               ("SAVINGS", "SAVINGS"),
               ]



# money in
# money out
# current balance - current balance after transaction has occured
# category - rent, youtube subscription, gym subscription, groceries week 1
# tag - want, needs, savings
# Payee - person recieving the payment e.g. landlord for rent
# date of transaction - date the transaction was made
# account - e.g. santander, monzo, halifax, monzo pot 1
# description/ notes - extra data about each transaction
# cleared - boolean of whether the transaction is cleared or not

class Transaction(models.Model):
    money_in = models.IntegerField()
    money_out = models.IntegerField()
    current_balance = models.IntegerField()
    category = models.CharField()
    tag = models.CharField(choices=TAG_CHOICES, default="--")
    payee = models.CharField()
    transaction_date = models.DateField()
    account = models.CharField()
    description = models.CharField()
    cleared = models.BooleanField()


    def _str_(self):
        return self.current_balance

