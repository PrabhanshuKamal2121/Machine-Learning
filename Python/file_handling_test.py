# Roadmap = open(r'Roadmap.txt')
# print(Roadmap.read())

# # Superman = open('superheroes.txt','w')
# # # w overwrite kar deta hai ya nahi present hoga to create that's why we use a(append)
# # Superman.write(f"this is good")

# r = open('superheroes.txt','a')
# r.write("append this and that")

# r.close()

# the project of file handling consists of 4 operations
# 1- to create a file
# we need a name+tell them to use update 3 button to write something/append in it 
# 2- reading a file
# we need to get file name, if not present tell them.
# 3- to update a file
# ask for name of file, update content text
# 4- to delete a file
#ask for name and delete it

from pathlib import Path
import os

print("1- to create a file")
print("2- reading a file")
print("3- to update a file")
print("4- to delete a file")

def showallfiles():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")
        # In Python, enumerate() is a built-in function that adds a counter to something you’re looping over.
        # rglob = recursive globe=sare things ko recurssive way me 

def createfile(name):
    try:
        r=open(name+'.txt','x')
        r.close()
    except Exception as err:
        print(err)

def readFile(name):
    try:
        r = open(name+'.txt','r')
        print(r.read())
        r.close()
    except Exception as err:
        print(err)

def update_file(name,content):
    try:
        r= open(name+'.txt','a')
        r.write(content)
        r.close()
    except Exception as err:
        print(err)

def delete_file(name):
    try:
        
        r = open(name+'.txt','r')
    except Exception as err:
        print(err)
        

button = int(input('enter your number:'))

if button==1:
    showallfiles()
    name = str(input('Enter your file name:'))
    createfile(name)

if button==2:
    showallfiles()
    name = str(input('Enter your file name:'))
    readFile(name)

if button==3:
    showallfiles()
    name = str(input('Enter your file name:'))
    content = str(input('Enter the content you want to be updated'))
    update_file(name,content)

if button==4:
    showallfiles()
    name = str(input('Enter your file name:'))
    delete_file(name)