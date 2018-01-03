# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:52:50 2018

@author: punee
"""
import pandas as pd
import os
import hashlib

def get_password():
    ''' Takes input for the password
        
            return type - string
    '''
    
    
    return input("Password : ")


def get_user_information():
    ''' Gets user information for storing in a csv file
    
            return type - pandas Series
        '''
        
    index_of_details = ['First Name' , 'Last Name' , 'e-mail id' , 'User Id' , 'Password']
    
    user_details = []
    
    for index in index_of_details:
        if index == 'Password' :
            password = get_password()
            hash_of_password = hashlib.sha3_256(password.encode()).digest()
            user_details.append(hash_of_password)
            continue
        user_details.append(input("{} : ".format(index)))
    
    return pd.Series(user_details, index = index_of_details)
    
def save_user_details(user_information):
    ''' Stores the data in a new file
    
        return type - none
    '''
    
    loction_to_store_details = os.getcwd()+"\\Database-Management\\user-accounts-details\\"
    filename = "userdetails"
    fileno = 0
    final_location = loction_to_store_details + filename + str(fileno)
    while(os.path.isfile(final_location)):
        final_location = loction_to_store_details + filename + str(fileno)
        fileno+=1
        
    user_information.to_csv(final_location)
    
def create_new_account():
    ''' Creates a new account
            stores user information in Database-Management/user-account-details
            password is stored as sha3_256 hash
            
            return type - none
        '''
    
    user_information = get_user_information()
    
    save_user_details(user_information)
    


