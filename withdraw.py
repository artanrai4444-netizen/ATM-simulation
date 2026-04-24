# withdraw.py
import utils


def withdraw():
    
    amt = int(input("Enter amount to withdraw: Rs. "))
    pin1= int(input("Enter PIN: "))

    if pin1!= utils.pin:
        print("Wrong PIN! Try again.")
    elif amt <= 0:
        print("Amount must be greater than 0.")
    elif amt > utils.bal:
        print("Insufficient balance! Available: Rs.", utils.bal)
    else:
        utils.bal -= amt
        utils.txns.append("DEBIT Rs." + str(amt) + " Bal: Rs." + str(utils.bal))
        print("Rs.",amt,"withdrawn successfully!")



    