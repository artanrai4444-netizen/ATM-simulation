import utils
import re

def deposit():
    acc = input("Enter account number: ")           
    if not re.fullmatch(r"[2-9]\S{11}$", acc):     
        print("Wrong account number.")
        return

    amount = int(input("Enter amount to deposit: Rs. "))
    if amount <= 0:
        print(" Deposit amount must be greater than 0.")
        return

    utils.bal += amount                           
    utils.txns.append("CREDIT Rs." + str(amount) + "  Bal: Rs." + str(utils.bal))
    print("Rs.", amount, "deposited successfully!")
