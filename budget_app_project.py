#The budget App Project is one of the projects required for my certification
#Made by Mayra Silva

class Category:
    def __init__(self, name): #name is used here to define the category
        self.name = name
        self.ledger = []
    

    def deposit(self, amount, description=''):
        if amount >=0:
            self.deposit = {"amount": amount, "description": description}
            self.ledger.append(self.deposit)

        return self.ledger
    


    def get_balance(self): # To get the total amount after transactions

        self.balance = 0

        for transaction in self.ledger:
            
            self.balance += transaction.get('amount')
        
        self.current_balance = self.balance

        return self.current_balance
    


    def check_funds(self, amount):
        if amount > self.current_balance:
            return False
        
        else:
            return True
    


    def withdraw(self, amount):

        if amount <= self.current_balance and self.check_funds(amount):
             self.withdraw = {'amount':  -amount, 'withdraw': True}
             self.ledger.append(self.withdraw)
             return True
        
        else:
            self.withdraw = {'amount': 0,  'withdraw': False}
            return False
        


    
    def transfer(self, amount, other_category):



    





        



    




def create_spend_chart(categories):
    pass


# Test lines:

books = Category("books")

print("Deposit: ", books.deposit(70, 'The way of the Kings'))
print("Current balance: ", books.get_balance())
print("Withdraw ", books.withdraw(70))
print("Current balance: ", books.get_balance())