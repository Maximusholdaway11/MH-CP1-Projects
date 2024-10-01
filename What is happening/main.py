#Max Holdaway What is happening?

#Creating a class for your banking system
class BankAccount:
    #Function to assist in individualalizing specific users
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    #Function for depositing money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    #Function for withdrawing money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    #Function for getting how much money you currrently have
    def get_balance(self):
        return self.balance

#Function for creating an account
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

#The "Main" function which acts as the banking system
def main():

    #Asking the user whether or not they want to choose between these five choices
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        #Getting the users choicec
        choice = input("Enter your choice (1-5): ")
        
        #If the user chose "1" allow them to create an account
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        #If the user chose "2" first have them login to the account
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]

                #Once logged in let the user deposit money
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")

                #If the user chose "3" let them withdrawl money
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        
        #If the user chose "5" exit the banking system
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        #If the user chose any number beside "1-5" then tell them it was invalid and did not work
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()