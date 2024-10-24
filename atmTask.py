# #Create an ATM application

# #requirements -
# #**** HDFC ATM ****

# #customer Name
# #card number
# #pin -  both card & pin are inputs from the user
# #balance - 1000

# #1. Deposit
# #2. Withdraw
# #3. exit

# #if the card number/pin matches with the input data proceed else print invalid.
# #if the choice is not one of the above, print invalid choice.

# # for persistent data we can use database, localStoragePy API, JSON storage.

# creating log files for the atm application. 

import logging
logging.basicConfig(filename="transaction.log", level=logging.INFO, format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s')


customers = [
    {
        "card": 12345,
        "pin": 1111,
        "name": "Akhil",
        "balance": 1000
    },
    {
        "card": 7895460,
        "pin": 2222,
        "name": "Arjun",
        "balance": 1000
    }
]

# Taking card number and PIN as inputs from the customer
cardNumber = int(input("Enter your card number: "))
pinNumber = int(input("Enter your PIN: "))

# Verifying the card number and PIN

for customer in customers:
    if customer["card"] == cardNumber and customer["pin"] == pinNumber:
        print("Hello", customer["name"], "Welcome to HDFC BANK")
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Fund Transfer")
            print("4. Exit")
            ch = input("Enter your choice: ")

            if ch == "1":
                amount = int(input("Enter amount to deposit: "))
                customer["balance"] += amount
                print("Your current balance is: ", customer["balance"])

            elif ch == "2":
                amount = int(input("Enter amount to withdraw: "))
                if amount > customer["balance"]:
                    logging.warning(f"{customer['name']} attempted to withdraw {amount}. Insufficient balance: {customer['balance']}.")
                    print("Insufficient balance")
                else:
                    customer["balance"] -= amount
                    print("Your current balance is: ", customer["balance"])

            elif ch == "3":
                payee_number = int(input("Enter the payee's card number: "))
                
                # Find the payee by looping through the customers list
                payee = None # initially set to None
                for p in customers:   # iterate over customers data and checks if the payee card number is same or not.
                    if p["card"] == payee_number:
                        payee = p
                        break

                if payee:  # check if payee exists
                    transfer_amount = int(input(f"Enter amount to transfer to {payee['name']}: "))
                    
                    if transfer_amount > customer["balance"]:
                        logging.warning(f"{customer['name']} transferred {transfer_amount} to {payee['name']}. Customer balance: {customer['balance']}")
                        print("Insufficient balance for transfer.")
                    else:
                        customer["balance"] -= transfer_amount
                        payee["balance"] += transfer_amount
                        logging.info(f"{customer['name']} transferred {transfer_amount} to {payee['name']}. New balance: {customer['balance']}")
                        print(f"Transfer successful! You transferred {transfer_amount} to {payee['name']}.")
                        print(f"Your current balance is: {customer['balance']}")
                else:
                    logging.error(f"Invalid payee card number entered by {customer['name']}.")
                    print("Invalid card number.")

            elif ch == "4":
                print("Thank you for banking with HDFC.")
                break
            else:
                print("Invalid choice. Please try again.")
        break
else:
    logging.info(cardNumber, pinNumber, customer['name'], customer['amount'], customer['balance'])
    print("Invalid card number or PIN. Please try again.")
