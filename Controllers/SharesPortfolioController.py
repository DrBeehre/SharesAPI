import sys
sys.path.insert(1, 'H:\Coding\Python\SharesAPI\Services')

import GatherService

#Creds
email = input("Please enter an email: ")
password = input("Please enter a password: ")

GatherService.get_values(email, password)