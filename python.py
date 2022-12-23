class bank:
    
    def __init__(self,initial_amount=0.00):
        self.balance = initial_amount
        
        
    def log_transaction(self,transaction_string):
        with open("transaction.txt","a") as file:
            file.write(f'{transaction_string}\t\t\t total Balance: {self.balance}\n')
          
    def withdrawl(self,amount):
            amount=float(amount)
            if amount:
             self.balance = self.balance - amount
             self.log_transaction(f'withdrew {amount}')
            
    def deposit(self,amount):
           amount=float(amount)
           if amount:
            self.balance = self.balance + amount
            self.log_transaction(f'deposited {amount}')
while True:
    account = bank(100.00)
    action = input('what action do you want to take\t\t 1-withdraw \t\t 2-Deposit \n choose any one')
    if action == "1":
        amount = input ('enter the amount')
        account.deposit(amount)             
    elif action== "2":
        amount = input ('enter the amount')
        account.withdrawl(amount) 
    else:
        print(f'you entered a wrong choice try to enter a valid choice') 
    
    print(f'your balance is {account.balance}')   
        
# print(account.balance)
# account.withdrawl(40.00)
# print(account.balance)
