#Library and Value
from random import * 
from prettytable import PrettyTable
from os import system,name
from time import sleep 
data = {25032:{'Name':'Naphop Khumchawna','Age':25,'money':10},24354:{'Name':'Veeraya Lekchaaum','Age':17,'money':40},74512:{'Name':'Klittima Chawwadee','Age':19,'money':50}}
bus_stop = {1:{'BName':'Busta Shinjuku','Price':5},2:{'BName':'Tomigaya','Price':10},3:{'BName':'Sakurabashi','Price':15},4:{'BName':'Namsan Seoul Tower','Price':20},5:{'BName':'Seoul Arts Center','Price':25},6:{'BName':'Myeong-dong Entrance','Price':30},7:{'BName':'Seoul Square','Price':35},8:{'BName':'Bridge St','Price':40},9:{'BName':'Manchester Coach Station','Price':45},10:{'BName':'Manchester Shudehill','Price':50}}

#Function
def name_program():
        print(''' ____              ____                                  _     ____            _                 
| __ ) _   _ ___  |  _ \ __ _ _   _ _ __ ___   ___ _ __ | |_  / ___| _   _ ___| |_ ___ _ __ ___  
|  _ \| | | / __| | |_) / _` | | | | '_ ` _ \ / _ \ '_ \| __| \___ \| | | / __| __/ _ \ '_ ` _ \ 
| |_) | |_| \__ \ |  __/ (_| | |_| | | | | | |  __/ | | | |_   ___) | |_| \__ \ ||  __/ | | | | |
|____/ \__,_|___/ |_|   \__,_|\__, |_| |_| |_|\___|_| |_|\__| |____/ \__, |___/\__\___|_| |_| |_|
                              |___/                                  |___/                       ''')
def clear():
    sleep(0.5)
    if name == 'nt':
        _ = system('cls')

def show_id(id):
    table_register = PrettyTable()
    name = data[id]['Name']
    money = data[id]['money']
    table_register.field_names = ['Your ID','Your Name','Balance']
    table_register.add_row([id,name,money])
    return print(table_register)
def farewell(name):
    print(f'\nThank You Have A Goodday {name}')

def check_id(id):
    if id in data.keys():
        return id
    else: 
        return 0

def gen_id():
    id = lambda x : str(randint(0,9))
    num = (''.join([id(i)for i in range (5)]))
    if num in data.keys():
        print('Has IT')
        num = (''.join([id(i)for i in range (5)]))
    # print(num)
    return int(num)

def register():
    while True:
        name_program()
        print('''
  _   _   _   _   _   _   _   _     _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
( R | e | g | i | s | t | e | r ) ( P | a | g | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 
''')
        try:
            id = gen_id()
            name = str(input("Your Name is : "))
            surname = str(input('Your Surname is : '))
            if name.isalpha() and surname.isalpha():
                if name !='' or surname != '':
                    age = int(input("Your Age is : "))    
                    fullname = name+' '+surname
                    for id_member in data.keys():
                        if fullname == data[id_member]['Name']:
                            input('Has this name on our database Please Try Again...') 
                            clear()
                            register() 
                    data[id] = {
                        'Name':fullname,
                        'Age':age,
                        'money':0
                        }
                    print('\nRegister Successfully ! ! !')
                    show_id(id)
                    input('Press Any Key To Continue....')
                    clear()
                    break
                else:
                    input('Your Name Or Surname Can not Blank Please Try Again ....')
                    clear()
            else:
                input('You Name or Surname Should be String not Number Please Try Again...')
        except ValueError: 
            input('Your Age Should Be Number Please Try Again...')
            clear()
def pay():
    while True:
        name_program()
        print('''  _   _   _   _   _   _   _     _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
( P | a | y | m | e | n | t ) ( P | a | g | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ ''')
        table_payment = PrettyTable()
        table_bus = PrettyTable()
        result_payment = PrettyTable()
        try: 
            # print(data)
            user_id=int(input("\nYour ID :"))
            if check_id(user_id) == user_id:
                table_payment.field_names = ['Your ID','Your Name','Balance']
                table_payment.add_row([user_id,data[user_id]["Name"],data[user_id]["money"]])
                print(table_payment)
                # print(data)
                table_bus.field_names=['NO.','Bus Stop Pitch']
                for select in bus_stop.keys():
                    table_bus.add_row([select,bus_stop[select]['BName']])
                print(table_bus)
                start=int(input("Choose Start Station : "))
                stop=int(input("Choose Stop Station : "))
                if start > stop:
                    print('Wrong Destination Please Try Again')
                    clear()
                    return 1
                elif start == stop:
                    print('Wrong Destination Please Try Again')
                    clear()
                    return 1
                start_b = bus_stop[start]['BName']
                stop_b = bus_stop[stop]['BName']
                user_age = data[user_id]['Age']
                pay=bus_stop[stop]['Price']-bus_stop[start]['Price']
                print(f'\n=====You are from {start_b} to {stop_b}=====')
                if user_age >=0 and user_age <= 20:
                    rate = 3
                    status = 'STUDYING AGE'
                elif user_age >=21 and user_age <= 59:
                    rate = 0
                    status = 'WORKING AGE'
                else:
                    rate = 2
                    status = 'OLD AGE'
                if pay>data[user_id]['money']:
                    print('\nYour balance is not sufficient')
                    choose = str(input('Would You Like To Top Up ? (y/n) : '))
                    if choose.lower() == 'y':
                        print('Redirect To Top-up Page')
                        clear()
                        top_up()
                        break
                    elif choose.lower() == 'n':
                        clear()
                        break 
                    else:
                        clear()
                        print('Please Try Again')
                        break                       
                else:
                    table_payment.clear_rows()
                    pay_discount=bus_stop[stop]['Price']-bus_stop[start]['Price']-rate
                    stable = data[user_id]['money']-pay_discount
                    data[user_id]['money'] = stable
                    result_payment.field_names=(['ID','Name','Age','Promotion','Full Price','Discount','Discount Price','Balance'])
                    result_payment.add_row([user_id,data[user_id]["Name"],user_age,status,pay,rate,pay_discount,stable])
                    print('\n',result_payment)
                    farewell(data[user_id]['Name'])
                    input('Press Any Key To Continue... ')
                    clear()
                    return 0
            else:
                print('Not Found Your ID Please Try Again')
                choose = str(input('Do You Want to Go To Main Menu ? (y/n) : '))
                if choose.lower() == 'y':
                    print('Redirect to Mainmenu')
                    clear()
                    break
                elif choose.lower()=='n':
                    clear()
                    pass
        except (TypeError,ValueError) as e : 
            input('It Should Be Number Please Try Again...')
            clear()
def top_up():
    while True:
        name_program()
        print('''
  _   _   _   _   _   _     _   _   _   _  
 / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
( T | o | p | - | U | p ) ( P | a | g | e )
 \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ ''')
        top_up_table = PrettyTable()
        final_table = PrettyTable()
        try:
            user_id=int(input("\nYour ID : "))
            if check_id(user_id) == user_id:
                money=data[user_id]['money']
                name=data[user_id]['Name']
                top_up_table.field_names=['ID','Name','Balance']
                top_up_table.add_row([user_id,name,money])
                print(top_up_table)
                topup=int(input('Top up : '))
                money += topup
                data[user_id]['money'] = money
                print('\nSuccessfully ! ! ! ! ')
                final_table.field_names=['ID','Name','TopUp','Balance']
                final_table.add_row([user_id,name,f'+{topup}',money])
                print(final_table)
                print('Thank You For Top Up')
                input('Press Any Key To Continue... ')
                clear()
                break
            else:
                print('Not Found This ID')
                choose = input('Do You Want to Register ? (y/n) : ')
                match choose.lower():
                    case 'y':
                        print('Redirect To Register Page....')
                        clear()
                        register()
                        break
                    case 'n':
                        clear()
                        break
        except (ValueError,TypeError) as e:
            input('Your Money Should Be Only Number Please Try Again...')
            clear()



# Main Programe

while True :
    name_program()
    try:
        print('What Would You Like :\n[0]Exit\n[1]Register\n[2]Pay\n[3]TopUP')
        choose = int(input('Choose : '))
        if choose <=3:
            match choose:
                case 0 :
                    break
                case 1 :
                    clear()
                    register()
                case 2 :
                    clear()
                    if pay() == 0:
                        break
                case 3 :
                    clear()
                    top_up()
        else:
            input('0 1 2 3 Only Please Try Again...')
            clear()
    except (ValueError,TypeError):
        input('Only Number Please Try Again...')
        clear()
