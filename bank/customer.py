
class Customer:

    customer_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Customer.customer_id
        self.accounts = []
        Customer.customer_id += 1

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
