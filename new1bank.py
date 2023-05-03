import json

ACCOUNTS_FILE = "accounts.json"

def load_accounts():
    try:
        with open(ACCOUNTS_FILE) as f:
            accounts = json.load(f)
    except FileNotFoundError:i
        accounts = []
    return accounts

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f)

accounts = load_accounts()

while True:
    print("Welcome to HONEY'S NATIONAL BANK ")
    print("1. TO CHECK BALANCE")
    print("2. TO WITHDRAW AMOUNT")
    print("3. TO DEPOSIT AMOUNT")
    print("4. TO OPEN NEW ACCOUNT")
    print("5. TO EXIT")

    choice = int(input("Enter any number to perform operation: "))

    if choice == 1:
        account_no = int(input("Enter account number: "))
        for account in accounts:
            if account["account_no"] == account_no:
                print("YOUR AVAILABLE BALANCE IS :", account["balance"])
                break
        else:
            print("Account not found. Please try again.")
    elif choice == 2:
        account_no = int(input("Enter account number: "))
        for account in accounts:
            if account["account_no"] == account_no:
                amount = float(input("Enter amount to withdraw: "))
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    print("You have withdrawn", amount)
                    print("Your available balance is:", account["balance"])
                else:
                    print("Insufficient funds")
                break
        else:
            print("Account not found. Please try again.")
    elif choice == 3:
        account_no = int(input("Enter account number: "))
        for account in accounts:
            if account["account_no"] == account_no:
                amount = float(input("Enter amount to deposit: "))
                account["balance"] += amount
                print("You have deposited", amount)
                print("Your current balance is", account["balance"])
                break
        else:
            print("Account not found. Please try again.")
    elif choice == 4:
        print("Please provide the following information to open a new account:")
        name = input("Full Name: ")
        balance = float(input("Initial Deposit Amount: "))
        account_no = len(accounts) + 1
        account = {
            "account_no": account_no,
            "name": name,
            "balance": balance
        }
        accounts.append(account)
        save_accounts(accounts)
        print("Account opened successfully! Your account number is", account_no)
    elif choice == 5:
        print("Thank you for using HONEY'S NATIONAL BANK")
        break
    else:
        print("Invalid input. Please try again.")
