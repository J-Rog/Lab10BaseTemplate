class Account:
    def __init__(self, balance=0, account_num=0):
        self._balance = balance
        self._account_num = account_num

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount < self._balance:
            self._balance -= amount
            return True
        else:
            return False
    def __str__(self):
        output = f'Account #: {self._account_num}\n'
        output += f'Current balance: {self._balance}'
        return output
    def __repr__(self):
        return( f'Account({self._balance}, {self._account_num})' )
