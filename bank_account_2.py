class BankAccount():
    # Methods
    
    def __init__(self, balance):
        self.balance = balance # attribute
        
    def deposit(self, amount):
        # amount = float(input("Enter the amount you want to deposit:"))
        self.amount = amount
        self.balance += self.amount

        print(f"Your deposit amount of ${self.amount:.2f} was successful. Your new balance is ${self.balance:.2f}")
        
    
    def withdraw(self, amount):
        # amount = float(input("Enter the amount you want to withdraw:"))
        self.amount = amount
        if self.amount > self.balance:
           print(f"Insufficient funds. Your current balance is ${self.balance:.2f}")
        else:
            self.balance = self.balance - self.amount 
            print(f"Your withdraw request of ${self.amount:.2f} was successful. Your new balance is ${self.balance:.2f}")
    
    def get_balance(self):
        print(f"Your current account balnce is ${self.balance:.2f}")
        

accounts = {
    'FGH-12345' : BankAccount(100000),
    'FGH-23689' : BankAccount(2003446), 
    'FGH-10965' : BankAccount(12345670),
    'FGH-12900' : BankAccount(90000)
} 
# We initialize the balance of the accounts with the class BankAccount
    
print("Welcome to our Bank. Please enter your account details.")


while True: # This loops over the whole program
    
    # A menu for the user
    print("\nThe following services are available:")
    
    print('1. Create account.')
    print('2. Deposit.')
    print('3. Withdraw.')
    print('4. Check Balance.')
    print('5. Exit.')
    
        
    choice = input("\nEnter the action you want to proceed with:")
    
    if choice == '1':
        print("If you wish to continue type in '1'. If otherwise type in '0'.")
        
        while True: # This loops over the program for creating a new account
            
            create_account = input("What is your choice: ")
            # this is where the user will input there choice if they are not sure yet using this they can go back
            
            if create_account == '1': # This handles diffrent  input from the user
                new_account = input("Enter the account number to be added: ") #prompts the user to input their account number so that it can be added
                
                if new_account in accounts: # This checks if the account number the user wanted to add already exist
                    print(f"The account with the account number {new_account} already exists")
                
                else: #if false the following code is run
                    balance = float(input("Enter your initial bank balance: "))
                    accounts[new_account] = BankAccount(balance) 
                    # Here the new account is added to the dictonary accounts and it is then attached to the balance the user inputs 
                    print(f"The account with the account number {new_account} was created successfully. Initial account balance ${balance}")
                    
                    break
            
            elif create_account == '0':
                print("Thank you for choosing us have a nice day!")
                
                break
    
    elif choice == '2':
        account_number = (input("Enter your account number:"))
            
        if account_number in accounts:
            amount = float(input("Enter the amount you want to deposit:"))
            accounts[account_number].deposit(amount)  
            # using accounts[accounts_number] the balance that is attached to that account number is the one that will undergo that operation
            
        else:
            print(f"The account with the account number {account_number} does not exist. Kindly create an account.")
            # This handles a case where the account number is not found
    
    elif choice == '3':
        account_number = (input("Enter your account number:"))
            
        if account_number in accounts:
            amount = float(input("Enter the amount you want to withdraw:"))
            accounts[account_number].withdraw(amount) 
            
        else:
            print(f"The account with the account number {account_number} does not exist. Kindly create an account.")
    
    elif choice == '4':
        account_number = (input("Enter your account number:"))
            
        if account_number in accounts:
            accounts[account_number].get_balance()  
            
        else:
            print(f"The account with the account number {account_number} does not exist. Kindly create an account.")
    
    elif choice == '5':
        print("Thank you for using our services. Have a nice day!")
        
        break
    
    else:
        print("Kindly enter one of the following choices(1,2,3,4, 0r 5 to exit).")
        print()
    
    