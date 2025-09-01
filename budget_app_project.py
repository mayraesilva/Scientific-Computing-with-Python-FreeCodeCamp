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

        balance = 0

        for transaction in self.ledger:
            
            balance += transaction.get('amount')
        
        current_balance = balance

        return current_balance
    


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        
        else:
            return True
    


    def withdraw(self, amount, description):


        if amount <= self.get_balance() and self.check_funds(amount):
             withdraw_transaction = {'amount':  -amount, 'withdraw': description}
             self.ledger.append(withdraw_transaction)
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
        
        
         # withdrawals
        max_description_size = 23
        max_char_amount = 7
        total_of_withdrawals = []

        for dictionary in self.ledger:

            if 'withdraw' in dictionary.keys():
                withdraw_description = dictionary.get('withdraw')
                withdraw_amount = f"{dictionary.get('amount'):.2f}"
                          

                if len(withdraw_description) > max_description_size:
                    withdraw_description = withdraw_description[:max_description_size]


                if len(withdraw_amount) > max_char_amount:
                    withdraw_amount = withdraw_amount[:max_char_amount]
            
                
                number_of_spaces_withdraw = 30 - (len(withdraw_description) + len(withdraw_amount))
                withdraws_done = withdraw_description + ' ' * number_of_spaces_withdraw + withdraw_amount
                total_of_withdrawals.append(withdraws_done)


        all_withdrawals = ''        
        for withdraw in total_of_withdrawals:
            all_withdrawals += withdraw + '\n'

        #total
        final_balance = f'Total: {self.get_balance():.2f}'
        final_result = category_title+ '\n' + initial_deposit + '\n' + all_withdrawals + final_balance

        return final_result






#Now we are going to create the function



def create_spend_chart(categories): #categories is a list
    
    categories_spend_chart = []
    total_spent_per_category = []
    total_amount_spent = 0
    total_spent_per_catagory_percentage = []

    #to get the transactions made in this category
    for category in categories:
        categories_spend_chart.append({category.name : category.ledger})
    
    
    # to get the amount withdraw in each category
    for dict_of_category in categories_spend_chart: 
        total_value_spent = 0
        
        for transactions in dict_of_category.values():
            
            for transaction in transactions:
                
                if "withdraw" in transaction.keys():
                    amount_spent = transaction.get('amount')
                    total_value_spent += amount_spent

        category_total_spend_chart = {key: total_value_spent for key in dict_of_category.keys()}
        total_spent_per_category.append(category_total_spend_chart)

    #print(total_spent_per_category)

    # to get the total amount spent
    for dict_of_category in total_spent_per_category:
        for category in dict_of_category.keys():
            total_amount_spent += dict_of_category.get(category)
    
    
    # to get the percentage spent in each category 
    for dict_of_category in total_spent_per_category:
        for category in dict_of_category.keys():
            amount = dict_of_category.get(category)
            category_percentage = (int((((amount / total_amount_spent) * 100)) // 10) * 10) # to get the percentage the way FCC expects
            category_percentage_dict = {category : category_percentage}
            total_spent_per_catagory_percentage.append(category_percentage_dict)
    
    print(total_spent_per_catagory_percentage)



    # Now let's go into the plot part

    title = 'Percentage spent by category'
    levels = [x for x in range(100,-10,-10)]
    #print(levels)

    levels_dict = {}

    for level in levels:
        if level == 100:            
            levels_dict[level] = f'{level}| '

        elif level == 0:
            levels_dict[level] = f'  {level}| '

        else:
            levels_dict[level] = f' {level}| '


        for dict_of_percentage in total_spent_per_catagory_percentage:
            for amount in dict_of_percentage.values():

                if amount >= level:
                    levels_dict[level] += 'o  '
                else:
                    levels_dict[level] += '  '
        

    for level in levels_dict.values():
        
        print(level)

    base_line = '    ' + '---' * len(total_spent_per_catagory_percentage) + '-'
    print(base_line)



    categories_name = []
    for dict_of_percentage in total_spent_per_catagory_percentage:
        for category in dict_of_percentage.keys():
            categories_name.append(category)

    print(categories_name)
    max_row_vertically = max(categories_name, key=len)
    print(max_row_vertically)
    rows_needed_vertically = len(max_row_vertically)
    quantity_of_categories = len(categories_name)

    rows = {} 
    for row_number in range(rows_needed_vertically):
        for category in categories_name:
            if row_number < len(category):
                rows[row_number] = '****' + category[row_number] +'**'
            else:
                rows[row_number] += '**'

    for row in rows.values():
        print(row)
            






        


        


    


    





                    










food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

clothing.withdraw(15.89, 'jacket')

create_spend_chart([food, clothing])