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
        if amount > self.get_balance():
            return False
        
        else:
            return True
    


    def withdraw(self, amount, description):

        # print("amount type:", type(amount))
        # print("desc type/len:", type(description), len(description))
        # print("balance:", self.get_balance())
        # print("ledger so far:", self.ledger)


        if amount <= self.get_balance() and self.check_funds(amount):
             self.withdraw_transaction = {'amount':  -amount, 'withdraw': description}
             self.ledger.append(self.withdraw_transaction)
             return True
        
        else:
            return False
        


    
    def transfer(self, amount, other_category):

        if self.check_funds(amount):
            self.withdraw = {'amount':  -amount, 'Transfer to ': other_category}
            self.ledger.append(self.withdraw)
            other_category.deposit(amount, f'Transfer from {other_category}')
            return True
        
        else:
            return False
        


    
    def output_request(self, amount, other_category):
        pass




    





        



    




def create_spend_chart(categories): #categories is a list
    pass

# Test lines:

# books = Category("books")

# print("Deposit: ", books.deposit(70, 'The way of the Kings'))
# print("Current balance: ", books.get_balance())
# print("Withdraw ", books.withdraw(70))
# print("Current balance: ", books.get_balance())

#Test lines provided by FCC

food = Category('Food')
print('Deposit: ', food.deposit(1000, 'deposit'))
print('Withdraw: ', food.withdraw(10.15, 'groceries'))
print('Current balance:', food.get_balance())



clothing = Category('Clothing')

print('withdraw: ', food.withdraw(15.80, 'restaurant and more food for dessert'))
print('Transfer', food.transfer(50, clothing))