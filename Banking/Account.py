from decimal import *


# Function to get the $$$ input from the user.
def operation(op_type: str):
    while True:
        value = input("Enter the ammount in $ to {} ".format(op_type))
        try:
            scratch = Decimal(value)  # Initialising decimal value
            assert abs(scratch.as_tuple().exponent) <= 2
            value = float(value)
            return value
        except Exception as error:
            print("Type a valid numeric $ ammount")


class Account:

    def __init__(self, start_bal: float, annual_int: float):
        self.start_bal = start_bal
        self.curr_bal = start_bal
        self.tot_deposit = 0.0
        self.num_deposit = 0
        self.tot_withdraw = 0.0
        self.num_withdraw = 0
        self.annual_int_rate = annual_int
        self.service_charge = []
        self.account_status = True
        self.deposit_list = []
        self.withdraw_list = []

    def deposit(self, acc_limit):
        value = operation("Deposit")
        self.curr_bal += value
        self.tot_deposit += value
        if self.account_status == False and self.curr_bal >= acc_limit:
            self.account_status = True
            self.num_deposit += 1
        elif self.account_status == False and self.curr_bal < acc_limit:
            self.curr_bal -= value
            self.tot_deposit -= value
            print("Account still inactive, deposit is not valid"
                  "increase the one time deposit amount to bring the balance above {}".format(acc_limit))
        else:
            self.num_deposit += 1
        print(self.curr_bal)
    def withdraw(self, acc_limit, checking):
        if self.account_status:
            value = operation("Withdraw")
            self.curr_bal -= value
            self.tot_withdraw += value
            self.num_withdraw += 1
            if self.curr_bal < acc_limit and not checking:
                self.account_status = False
                print("Account is now inactive, increase it to {} to withdraw".format(acc_limit))
            elif self.curr_bal < acc_limit:
                # No enough funds in checking, withdraw canceled
                self.curr_bal -= 15 #Service charge now, not end of month
                self.curr_bal += value
                self.tot_withdraw -= value
                self.num_withdraw -= 1
        else:
            print("Account is now inactive, increase it to {} to withdraw".format(acc_limit))
        print(self.curr_bal)
    def calc_interest(self):
        monthly_int_rate = (self.annual_int_rate / 12)
        monthly_int = self.curr_bal * monthly_int_rate
        self.curr_bal += monthly_int
        return self.curr_bal

    def close_month(self):
        self.curr_bal -= sum(self.service_charge)
        self.calc_interest()
        self.num_withdraw = 0
        self.num_deposit = 0
        #Print Da stuff

        print('#'*30)
        print('Starting balance: {0:12.2f}'.format(self.start_bal))
        print('Total amount of deposits: {0:26.2f}'.format(self.tot_deposit))
        print('Total amount of withdrawals: {0:26.2f}'.format(self.tot_withdraw))
        print('Total amount of service charge: {0:26.2f}'.format(sum(self.service_charge)))
        print('Account Status'.format(self.account_status))





