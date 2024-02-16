# services.py
from .models import Account

def create_account(user, data):
    account = Account.objects.create(user=user, **data)
    return account
