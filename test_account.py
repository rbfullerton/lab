from account import Account
from pytest import *

def test_init():
    account_one = Account('John')
    assert account_one.get_name() == 'John'
    assert account_one.get_balance() == 0

def test_deposit():
    account_one = Account('John')
    assert account_one.deposit(1000000) is True
    assert account_one.deposit(-1000000) is False
    assert account_one.deposit(0) is False
    assert account_one.get_balance() == approx(1000000,abs=0.001)

def test_withdraw():
    account_one = Account('John')
    assert account_one.deposit(1000000) is True
    assert account_one.withdraw(500000) is True
    assert account_one.withdraw(750000) is False
    assert account_one.withdraw(-750000) is False
    assert account_one.withdraw(0) is False
    assert account_one.get_balance() == approx(500000,abs=0.001)
