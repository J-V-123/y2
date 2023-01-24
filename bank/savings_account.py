from account import Account


class SavingsAccount(Account):

    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, sum):
        if self.balance >= sum and account.get_customer() == self.owner:
            self.balance -= sum
            account.deposit(sum)
            return True
        else:
            return False
