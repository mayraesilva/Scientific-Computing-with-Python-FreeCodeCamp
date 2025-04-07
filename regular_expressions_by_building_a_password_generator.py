#Beginning
import random
import secrets
import string



def generate_password(length):
    #Define the possible characters for the password
    letters = string.ascii_letters #these are the letters abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits #these are the digits 0123456789
    symbols = string.punctuation # these are the symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


    #Combine all characters
    all_characters = letters + digits + symbols

    # print(all_characters)
    # print(secrets.choice(all_characters))

    password = ''

    #Generate password
    for i in range(length):
        password += secrets.choice(all_characters) 
    




