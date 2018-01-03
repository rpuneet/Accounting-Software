# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:01:18 2018

@author: Puneet
"""
import hashlib
PASSWORD = hashlib.sha3_256("this is the password".encode())
hash_password = PASSWORD.digest()

def login(user_id , password):
    
    global hash_password
    hash_input_password = ''
    input_password = input("Enter Password : ")
    hash_input_password =  hashlib.sha3_256(input_password.encode()).digest()
    if (hash_input_password == hash_password):
        return True
    print("Wrong Password.")
    return False

            