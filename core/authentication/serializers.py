from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'money_in', 'money_out', 'current_balance', 'category', 'tag', 'payee', 'transaction_date', 'account', 'description', 'cleared')