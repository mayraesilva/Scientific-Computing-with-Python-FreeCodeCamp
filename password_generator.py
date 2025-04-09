#Beginning the password generator

#import random #We were going to use it, but it becomes predictible, not so goo for a passcode
import re
import secrets
import string



def generate_password(length, nums, special_chars, uppercase, lowercase):
    #Define the possible characters for the password
    letters = string.ascii_letters #these are the letters abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits #these are the digits 0123456789
    symbols = string.punctuation # these are the symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


    #Combine all characters
    all_characters = letters + digits + symbols

    # print(all_characters)
    # print(secrets.choice(all_characters))

    while True:

        password = ''

        #Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [(nums, r'\d'), #replace [0-9] with \d (same effect)
                       (lowercase, r'[a-z]')
                       (uppercase, r'[A-Z]'),
                       (special_chars,  r'\W')] #Replace the [^a-zA-Z0-9] character class with \W
        
          # Check constraints

        count = 0

        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)): #You are interested in the number of elements in the list returned by the findall() function.
                count += 1
        
        if count == 4:
            break

    return password

# pattern = re.compile('l+') 
# quote = 'Not all those who wander are lost.'
# print(pattern.search(quote)) #search for the character that matches in compile

# #Another ways is:
# pattern = 'l+'
# quote = 'Not all those who wander are lost.'
# print(re.search(pattern, quote))


# pattern = 't[a-z]' # t e depois a-z
# # pattern = '[a-z]t' # a-z e depois t
# quote = 'Not all those who wander are lost.'
# print(re.findall(pattern, quote)) #findall to check if the generated password meets the required features



# new_password = generate_password(8)
# print(new_password)

    




