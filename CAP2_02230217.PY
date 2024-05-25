class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self):
        account_number = len(self.accounts) + 1
        account = Account(account_number, 0)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Main function to interact with the user
def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Simple Banking Application")
        print("1. Open an Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = bank.open_account()
            print(f"Account created successfully. Your account number is {account_number}")
        elif choice == '2':
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                if account.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid amount.")
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance or invalid amount.")
            else:
                print("Account not found.")
        elif choice == '4':
            print("Thank you for using the Simple Banking Application")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
