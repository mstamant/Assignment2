from Account import *


class Checking_Account(Account):

    def __init__(self, start_bal: float, annual_int: float):
        super().__init__(start_bal,annual_int)
        self.acc_limit = 0
        self.checking = True

    def withdraw(self, acc_limit, checking):
        Account.withdraw(self, acc_limit, checking)
        self.service_charge.append(0.10)


    def close_month(self):
        self.service_charge.append(5)
        Account.close_month(self)
