import sys
sys.path.insert(1, 'H:\Coding\Python\SharesAPI\Services')

import GatherService

#Creds
email = 'wardbeehre@gmail.com'
password = 'BarKeri12345'

GatherService.get_values(email, password)