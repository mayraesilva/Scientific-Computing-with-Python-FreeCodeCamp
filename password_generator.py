#Beginning the password generator by Mayra Silva

#import random #We were going to use it, but it becomes predictible, not so goo for a passcode
import re
import secrets
import string



def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1): #default parameters
    #Define the possible characters for the password
    letters = string.ascii_letters #these are the letters abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits #these are the digits 0123456789
    symbols = string.punctuation # these are the symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


    #Combine all characters
    all_characters = letters + digits + symbols

    
    while True:

        password = ''

        #Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'), #replace [0-9] with \d (same effect)
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars,  r'\W') #Replace the [^a-zA-Z0-9] character class with \W
        ]
          # Check constraints

        

        
        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints): #generator expression can save memory
            break

    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)




    




