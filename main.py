import utils
from withdraw import withdraw
from depo  import deposit
from statement import show



def show_bal():
    print("\n--- Account Balance ---")
    print("Name   :", utils.name)
    print("Balance: Rs.", utils.bal)

while True:
    print("\n1. Deposit  2. Withdraw  3. Balance  4. Transactions  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        show_bal()
    elif choice == "4":
        show()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")