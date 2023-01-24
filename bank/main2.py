from bank import Bank
from customer import Customer


# korjaa sanakirja
def main():
    bank = Bank("The Best Bank")
    name_1 = "Seppo"
    name_2 = "Teppo"
    customer_1 = Customer(name_1)
    customer_2 = Customer(name_2)
    customer_3 = Customer(name_1)
    bank.add_customer(customer_1)
    bank.add_customer(customer_2)
    bank.add_customer(customer_3)

    account_1a = bank.add_account(customer_1)
    account_1b = bank.add_account(customer_1)
    account_2 = bank.add_account(customer_2)
    account_1a.deposit(100)
    account_1b.deposit(20)

    print_balance(account_1a, name_1)
    print_balance(account_1b, name_1)
    print_balance(account_2, name_2)
    print("")

    sum_to_transfer = 10
    if account_1a.transfer_to(account_2, sum_to_transfer):
        print("Transfer of {} units complete!".format(sum_to_transfer))
    else:
        print("Transfer of {} units failed!".format(sum_to_transfer))

    print("")
    print_balance(account_1a, name_1)
    print_balance(account_1b, name_1)
    print_balance(account_2, name_2)

    print("")

    print("")
    print("Get customer 1 by name: {}".format(bank.get_customers_by_name(name_1)))
    print("Get customer 2 by name: {}".format(bank.get_customers_by_name(name_2)))

    print("")
    print("Get customer 1 by id: {}".format(bank.get_customer_by_id(customer_1.get_id())))
    print("Get customer 2 by id: {}".format(bank.get_customer_by_id(customer_2.get_id())))
    print("Get customer 3 by id: {}".format(bank.get_customer_by_id(customer_3.get_id())))


def print_balance(account, name):
    print("{} has a balance of {}".format(name, account.get_balance()))


if __name__ == "__main__":
    main()
