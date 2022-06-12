from Account import *


class Saving_Account(Account):

    def __init__(self, start_bal: float, annual_int: float):
        super().__init__(start_bal,annual_int)
        self.acc_limit = 25
        self.checking = False

    def withdraw(self, acc_limit, checking):
        Account.withdraw(self, acc_limit, checking)

    def deposit(self, acc_limit):
        Account.deposit(self, acc_limit)

    def close_month(self):

        if self.num_withdraw > 4:
            for i in range(self.num_withdraw - 4):
                self.service_charge.append(1)

        Account.close_month(self)
