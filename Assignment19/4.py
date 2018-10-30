class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = float(balance)

    def __str__(self):
        return "Balance: {0:.2f}".format(self.balance)

    def update_balance(self):
        self.balance = (self.balance * 1.15)

class DebitAccount(SavingsAccount):
    def __init__(self, balance=0):
        SavingsAccount.__init__(self, balance)

    def update_balance(self):
        self.balance = (self.balance * 1.02)