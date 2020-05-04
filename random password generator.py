#Lilly Lewis CS II Final Project
#random password generator

import random #function for choosing characters at random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890!@#$%^&*()" #inserting characters to be chosen at random

tries = 0

while True:
    tries += 1
    number = input("How many passwords do you want? ")
    number = int(number)

    length = input("How long do you want your passwords? ")
    length = int(length)

    for i in range(number):
        password = ""
        for i in range(length):
            password += random.choice(chars)
        print(password)
        
    if tries >= 3:
        
        print ("game over")
        break
    

    