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


        if amount <= self.get_balance() and self.check_funds(amount):
             self.withdraw_transaction = {'amount':  -amount, 'withdraw': description}
             self.ledger.append(self.withdraw_transaction)
             return True
        
        else:
            return False
        


    
    def transfer(self, amount, other_category):

        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        
        else:
            return False
        


    
    def __repr__(self):
        stars = '******************************'
        #Name of class between stars
        category_length = len(self.name)
        left_pad = int(((len(stars) - category_length))/ 2)
        right_pad = (len(stars) - len(self.name) - left_pad)
        category_title = left_pad * '*' + self.name + right_pad * '*'
        

        #initial deposit
        #print(self.ledger)
        initial_deposit_value = self.ledger[0].get('amount')
        initial_deposit_string = 'initial deposit'
        initial_deposit_value_as_string = f'{initial_deposit_value:.2f}'

        number_of_spaces = 30 - (len(initial_deposit_string) + len(initial_deposit_value_as_string))
        initial_deposit = initial_deposit_string + ' ' * number_of_spaces +initial_deposit_value_as_string
        
        
         # withdraws
        max_description_size = 23
        total_of_withdraws = []
        for dictionary in self.ledger:
            if 'withdraw' in dictionary.keys():
                withdraw_amount = f"{dictionary.get('amount'):.2f}"
                withdraw_description = dictionary.get('withdraw')

                if len(withdraw_description) > max_description_size:
                    withdraw_description = withdraw_description[:max_description_size]
            
                
                number_of_spaces_withdraw = 30 - (len(withdraw_description) + len(withdraw_amount))
                withdraws_done = withdraw_description + ' ' * number_of_spaces_withdraw + withdraw_amount
                total_of_withdraws.append(withdraws_done)


        all_withdraws = ''        
        for withdraw in total_of_withdraws:
            all_withdraws += withdraw + '\n'

        #total
        final_balance = f'Total: {self.get_balance():.2f}'
        final_result = category_title+ '\n' + initial_deposit + '\n' + all_withdraws + final_balance

        return final_result












    




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
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)