
class Account():
    def __init__(self, name: str):
        '''
        get account name and balance
        Balance starts at 0
        :param name:  to be set account
        '''
        self.account_name = name
        self.account_balance = 0
    def deposit(self, amount):
        '''
        check deposit amount add to original amount
        :param amount: how much money to add
        '''
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self, amount):
        '''
        function to take away from your account
        check account > 0
        :param amount: how much money to take
        '''
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance = amount
                return True
        return False
    def get_balance(self):
        '''
        get account balance
        '''
        return self.account_balance
    def get_name(self):
        '''
        get account name
        '''
        return self.account_name



