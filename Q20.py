'''Q20. Write Python Program to Simulate a Bank Account for deposit, withdrawal and balance
Operations.'''
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. New balance: {self.balance}")
        else:
            print("Insufficient balance. Withdrawal failed.")
    
    def check_balance(self):
        print(f"Account balance: {self.balance}")

# Create a BankAccount object
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, initial_balance)

# Perform bank operations
while True:
    print("\nBank Account Operations:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Thank you for using the Bank Account Simulation. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
