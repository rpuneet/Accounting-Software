# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:26:06 2018

@author: rPuneet
"""
from create_new_account import *
from login import *


def get_option():
    ''' Gets choice from user for different options 
            
            return type - int
                (option_number)
    '''
    print("1. Login.\n2. Create New Account.")
    option_number = int(input("Enter Your option :"))
    
    if(option_number not in {1,2}):
        print("Invalid choice.\n")
        return get_option()

    return option_number
    
    

def initialise():
    ''' This function is the starting page of the software
        
            return type - none
    '''
    option_type = get_option()
    
    if option_type == 1 :
        login()
    else :
        create_new_account()
        
    