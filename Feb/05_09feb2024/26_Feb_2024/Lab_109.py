                              # Real time e.g

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("Your Bal", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def do_with_by_bank_manager(self, amount):
        self._withdraw(amount=amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)                                  # Public function
jp_chase.do_with_by_bank_manager(499)                   # Protected function
# jp_chase.if_you_are_auth(True)
jp_chase.if_you_are_auth(False)                         # Private function

jp_chase.public_fn()