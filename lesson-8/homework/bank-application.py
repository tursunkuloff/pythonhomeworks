import json

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient balance or invalid amount."

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        if initial_deposit < 0:
            return "Initial deposit cannot be negative."
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created. Account Number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account: {account.account_number}, Name: {account.name}, Balance: ${account.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.accounts.items()}, file)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.accounts = {int(k): Account.from_dict(v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

# Example usage
if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            deposit = float(input("Enter Initial Deposit: "))
            print(bank.create_account(name, deposit))
        elif choice == "2":
            acc_num = int(input("Enter Account Number: "))
            print(bank.view_account(acc_num))
        elif choice == "3":
            acc_num = int(input("Enter Account Number: "))
            amount = float(input("Enter Deposit Amount: "))
            print(bank.deposit(acc_num, amount))
        elif choice == "4":
            acc_num = int(input("Enter Account Number: "))
            amount = float(input("Enter Withdrawal Amount: "))
            print(bank.withdraw(acc_num, amount))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
