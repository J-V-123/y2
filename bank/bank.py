from account import Account
from customer import Customer
from personal_account import PersonalAccount
from savings_account import SavingsAccount


class Bank:

    def __init__(self, name):
        self.name = name
        self.customers = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customers

    def get_customers_by_name(self, name):
        customers_by_name = []
        for customer in self.customers:
            if customer.get_name() == name:
                customers_by_name.append(customer)
        return customers_by_name

    def get_customer_by_id(self, id):
        for customer in self.customers:
            if customer.get_id() == id:
                return customer
        return None

    #def add_account(self, customer):
     #   if customer in self.customers:
      #      new_account = Account(customer)
       #     customer.accounts.append(new_account)
        #    return new_account
        #else:
         #   return None

    def add_personal_account(self, customer):
        if customer in self.customers:
            new_account = PersonalAccount(customer)
            customer.accounts.append(new_account)
            return new_account
        else:
            return None

    def add_savings_account(self, customer):
        if customer in self.customers:
            new_account = SavingsAccount(customer)
            customer.accounts.append(new_account)
            return new_account
        else:
            return None

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

    def get_accounts(self, customer):
        if customer in self.customers:
            return customer.accounts
