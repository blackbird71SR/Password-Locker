#! python3
#
    # Omkar Ajnadkar
    # Category: Python Projects
    # Name: Password Locker
    # Website: https://thecodingexpress.blogspot.in
    # Twitter: @theCodingExprs
    # Gmail: thecodingexpress@gmail.com
#

import pyperclip,time,sys,json
from pathlib import Path

file = "pass.txt"
filePath = Path("pass.txt")
if filePath.is_file():
    open(file,"r+")
    passwords = json.load(open(file))
else:
    open(file,"w")
    passwords = {}
    print("This ")

def menu():
    print("---------------------")
    print("Password Locker")
    print("---------------------")
    print("1. Find password")
    print("2. Add password")
    print("3. Exit")
    print("---------------------")

    option = int(input("Enter option:"))

    while option:
        if option == 1: 
            findPassword()
        elif option == 2:
            savePassword()
        elif option == 3:
            break
        else:
            print("Invalid Option")
        print("-------------")
        option = int(input("Enter option:"))

    print("Exiting...")
    print("---------------------")


def savePassword():
    account = input("Enter website\email:")
    password = input("Enter password:")
    passwords[account] = encode(password)
    json.dump(passwords, open(file,"w"))
    print("Password Saved")

def findPassword():
    account = input("Enter website\email:")
    if account in passwords.keys():
        encrypted_pass = passwords[account]
        pyperclip.copy(decode(encrypted_pass))
        print("Password copied for 10 seconds...")
        time.sleep(10)
        pyperclip.copy("")
        print("Password destroyed from clipboard")
    else:
        print("Account not found")

def encode(password):
    encoded_chars= []
    for i in range(len(password)):
        encoded_c = chr(ord(password[i]) - len(password))
        encoded_chars.append(encoded_c)
    encrypted_pass = "".join(encoded_chars)
    return encrypted_pass
        
def decode(encrypted_pass):
    decoded_chars = []
    for i in range(len(encrypted_pass)):
        decoded_c = chr(ord(encrypted_pass[i]) + len(encrypted_pass))
        decoded_chars.append(decoded_c)
    decoded_pass = "".join(decoded_chars)
    return decoded_pass

menu()
