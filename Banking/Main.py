from Account import *
from Saving_account import *
from Checking_account import *
from menu import *


check = Checking_Account(5.0, 1.0)
check.account_status = True
saving = Saving_Account(25.0, 2)
saving.account_status = True



# Bank menu
def bank_menu():
    bank_menu_sel = ['A', 'B', 'C']
    while True:
        print("Bank Menu")
        print("A: Savings")
        print("B: Checking")
        print("C: Exit")
        usr_input = input().upper()
        try:
            assert (usr_input in bank_menu_sel)
            # return usr_input
            if usr_input == "A":
                savings_menu()
            elif usr_input == "B":
                checking_menu()
            elif usr_input == "C":
                break
        except Exception as error:
            print()  # Do Nothing like an ATM


# Savings menu
def savings_menu():
    account_menu_sel = ['A', 'B', 'C', 'D']
    while True:
        print("Savings Menu")
        print("A: Deposit")
        print("B: Withdrawal")
        print("C: Report")
        print("D: Return to Bank Menu")
        usr_input = input().upper()
        try:
            assert (usr_input in account_menu_sel)
            if usr_input == "A":
                saving.deposit(25.0)
            elif usr_input == "B":
                saving.withdraw(25.0, False)
            elif usr_input == "C":
                saving.close_month()
            else:
                break
        except Exception as error:
            print()  # Do Nothing like an ATM


# Checking menu
def checking_menu():
    while True:
        account_menu_sel = ['A', 'B', 'C', 'D']
        print("Checking Menu")
        print("A: Deposit")
        print("B: Withdrawal")
        print("C: Report")
        print("D: Return to Bank Menu")
        usr_input = input().upper()
        try:
            assert (usr_input in account_menu_sel)
            if usr_input == "A":
                check.deposit(0.0)
            elif usr_input == "B":
                check.withdraw(0.0, True)
            elif usr_input == "C":
                check.close_month()
            else:
                break
        except Exception as error:
            print()  # Do Nothing like an ATM

bank_menu()
