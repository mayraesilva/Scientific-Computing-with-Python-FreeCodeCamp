#The budget App Project is one of the projects required for my certification
#Made by Mayra Silva

class Category:
    def __init__(self, name): #name is used here to define the category
        self.name = name
        self.ledger = []
    

    def deposit(self, amount, description=''):
        self.deposit = {"amount": amount, "description": description}
        self.ledger.append(self.deposit)
        return self.ledger
        



    




def create_spend_chart(categories):
    pass


# Test lines:

books = Category("books")

print("Deposit: ", books.deposit(70, 'The way of the Kings'))