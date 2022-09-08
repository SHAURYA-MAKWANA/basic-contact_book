import json
import pandas as pd

print('**Made by Shaurya Makwana**')

address = {'name':'contact'}
path = open(r"data.json", 'r+')
data = ''

print('''do you want to add or see the contact
add - to create new contact
get - to find a contact of person
edit - to edit a contact
show - to see the contactbook ''')

res = input('what you want in contactbook: ')  


def show_address():
  global address
  address = json.load(path)
  print(address)

def update_address():
    pathw = open(r"data.json", 'w')
    json.dump(address,pathw)

def add_contact():
    show_address()
    x = input('enter the name of the person: ')
    y = input('enter the number of the person: ')
    address[x] = y
    print(address)
    update_address()

def edit_contact():
    show_address()
    x = input('enter the name of the person whose contact you want to edit: ')
    
    if x in address:
        pass
    else: 
        print('name not found please save it!!')
        return None    

    y = input(f'enter the number to change of the person from {address[x]}: ')
    address[x] = y
    print(address)
    update_address()
    print('name changed successfully')

def get_contact():
   show_address()
   x = input('enter name whose number you want to see: ')
   y = address.get(str(x))

   if y == None:
    print('Not found!!')
   else: print(address[x])

def excelify():
  show_address()
  df = pd.DataFrame(address, index=[0])
  df.to_csv('') #enter path where you want to save your file



if res == 'add':
  add_contact()
elif res == 'get':
  get_contact()
elif res == 'edit':
  edit_contact()
elif res == 'show':
  show_address()
elif res == 'excelify':
  excelify()
else: print('invalid input!')
