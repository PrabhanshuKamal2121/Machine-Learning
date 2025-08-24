import json
import random
import string
from pathlib import Path



class bank:
    def createacount(self):
        pass
    

user = bank()
print("press 1 for creating an account")
print("press 2 for deposting the money in the bank")
print("press 3 for withdrawinh the money")
print("press 5 for updating the details")
print("press 6 for deleting the account")

account = int(input("what you want to do?"))
if account ==1:
    user.createaccount()
elif account==2:
    print("")

