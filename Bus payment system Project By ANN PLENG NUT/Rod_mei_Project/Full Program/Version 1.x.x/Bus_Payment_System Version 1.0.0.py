#Library and Value

from random import *
from prettytable import PrettyTable
from os import system,name
from time import sleep

data = {25032:{'Name':'Naphop Khumchawna','Age':25,'money':100,'Status':'WORKING AGE'},24354:{'Name':'Veeraya Lekchaaum','Age':17,'money':40,'Status':'STUDYING AGE'},74512:{'Name':'Klittima Chawwadee','Age':19,'money':50,'Status':'STUDYING AGE'}}
bus_stop = {1:{'BName':'Busta Shinjuku','Price':5},2:{'BName':'Tomigaya','Price':10},3:{'BName':'Sakurabashi','Price':15},4:{'BName':'Namsan Seoul Tower','Price':20},5:{'BName':'Seoul Arts Center','Price':25},6:{'BName':'Myeong-dong Entrance','Price':30},7:{'BName':'Seoul Square','Price':35},8:{'BName':'Bridge St','Price':40},9:{'BName':'Manchester Coach Station','Price':45},10:{'BName':'Manchester Shudehill','Price':50}}

#Function of ADMIN
def admin_head():
    print('''
          _____  __  __ _____ _   _ 
    /\   |  __ \|  \/  |_   _| \ | |
   /  \  | |  | | \  / | | | |  \| |
  / /\ \ | |  | | |\/| | | | | . ` |
 / ____ \| |__| | |  | |_| |_| |\  |
/_/    \_\_____/|_|  |_|_____|_| \_|\n''')

def login_admin():
        while True:
            try:
                admin_head()
                print('\nCtrl + c To Exit Admin mode .....\n')
                # username = 'admin'
                # password = 'admin'
                username = str(input('Username : '))
                password = str(input('Password : '))
                if username == 'admin' and password == 'admin':
                    print("Welcome Admin")
                    clear()
                    admin_menu()
                else:
                    input('Wrong Please Try Again....')
                    clear()
            except KeyboardInterrupt:
                print('Exit Admin Mode...')
                clear()
                break
        
def admin_menu():
    while True:
        try :
            admin_head()
            choose = int(input('[0]Log Out\n[1]Edit\n[2]Delete\n[3]Find\nWhat Would You Like To Do ? : '))
            if choose >= 0 and choose <=3:
                match choose:
                    case 1:
                        clear()
                        edit_admin()
                        break
                    case 2:
                        clear()
                        delete_admin()
                        break
                    case 3:
                        clear()
                        find_admin()
                        break
                    case 0:
                        clear()
                        break
            else:
                clear()
                admin_menu()
                break
        except ValueError:
            print('0 1 2 3 Only Please Try Again')
            clear()
            admin_menu()
        except KeyboardInterrupt :
            print('Exit Admin Menu Select....')
            clear()
            break

def table_user():
    user_table = PrettyTable()
    user_table.field_names = ['ID','NAME','AGE','STATUS','BALANCE']
    for id in data.keys():
        name = data[id]['Name']
        status = data[id]['Status']
        balance = data[id]['money']
        age = data[id]['Age']
        user_table.add_row([id,name,age,status,balance])
    print(user_table) 

def edit_admin():
    while True:
        admin_head()
        print('''  _   _   _   _     _   _   _   _  
 / \ / \ / \ / \   / \ / \ / \ / \ 
( E | d | i | t ) ( U | s | e | r )
 \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 
''')
        pick_table = PrettyTable()
        try:
            table_user()
            edit_id = int(input('Edit ID : '))
            if check_id(edit_id) == edit_id:
                edit_choose = int(input('\nEDIT NAME OR AGE ?\n[0]Exit This Menu\n[1]Name\n[2]Age\nChoose : '))
                if edit_choose <= 2:
                    match edit_choose:
                        case 0 :
                            break
                        case 1 :
                            pick_table.field_names = ['ID','NAME'] 
                            pick_table.add_row([edit_id,data[edit_id]['Name']])
                            print(pick_table)
                            name = str(input('Name : '))
                            surname = str(input('Surname : '))
                            fullname = name + ' ' + surname
                            print('\nPlease Wait...')
                            sleep(1)
                            data[edit_id]['Name'] = fullname
                            pick_table.del_row(0)
                            pick_table.add_row([edit_id,data[edit_id]['Name']])
                            print('\nEdit Successfully ! ! ! !')
                            print(pick_table)
                            con = str(input('\nDo you want to Edit Continue ? (y/n) :'))
                            if con.lower() == 'y':
                                clear()
                                edit_admin()
                            elif con.lower() == 'n':
                                print('Go to Main Admin Menu....')
                                clear()
                                admin_menu()
                        case 2 :
                            pick_table.field_names = ['ID','NAME','AGE','STATUS']
                            pick_table.add_row([edit_id,data[edit_id]['Name'],data[edit_id]['Age'],data[edit_id]['Status']])
                            print(pick_table)
                            age = int(input('Edit Age : '))
                            if age >= 1 and age <= 20:
                                status = 'STUDYING AGE'
                            elif age >= 21 and age <= 59:
                                status = 'WORKING AGE'
                            elif age >=60: 
                                status = 'OLD AGE'
                            else: 
                                input('Your Age Can not be Zero Please Try Again...')
                                clear()
                                edit_admin()
                                break
                            print('\nPlease Wait...')
                            sleep(1)
                            data[edit_id]['Age'] = age
                            data[edit_id]['Status'] = status
                            pick_table.del_row(0)
                            pick_table.add_row([edit_id,data[edit_id]['Name'],data[edit_id]['Age'],data[edit_id]['Status']])
                            print('Edit Successfully ! ! ! !')
                            print(pick_table)
                            con = str(input('Do you want to Edit Continue ? (y/n) : '))
                            if con.lower() == 'y':
                                clear()
                                edit_admin()
                            elif con.lower() == 'n':
                                print('Go to Main Admin Menu....')
                                clear()
                                admin_menu()
                            else:
                                print('Go to Main Admin Menu....')
                                clear()
                                admin_menu()
                else : 
                    input('0 or 1 or 2 Only Please Try Again...')
                    clear()
            else: 
                input('Not Found This ID Please Try Again ...')
                clear()
        except ValueError as e :
            # print(e)
            input('Number Only Please Try Again...')
            clear()
        except KeyboardInterrupt :
            print('Exit Edit User Menu ...')
            clear()
            admin_menu()
            break
            


def delete_admin():
    while True:
        admin_head()
        print('''  _   _   _   _   _   _     _   _   _   _  
 / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
( d | e | l | e | t | e ) ( u | s | e | r )
 \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 
''')
        delete_table = PrettyTable()
        table_user()
        try: 
            delete_id = int(input('Delete ID : '))
            if delete_id in data.keys():
                delete_table.field_names=['ID','NAME','AGE','STATUS','BALANCE']
                delete_table.add_row([delete_id,data[delete_id]['Name'],data[delete_id]['Age'],data[delete_id]['Status'],data[delete_id]['money']])
                delete_com = int(input("Do You Want To Delete ?\n[0]Yes\n[1]No\nChoose: "))
                if delete_com == 0:
                    print('Please Wait...')   
                    sleep(1)               
                    del data[delete_id]
                    print('\nDelete successfully ! ! !')
                    table_user()
                    con = str(input('\nDo You Want to Continue ?(y/n): '))
                    if con.lower() == 'y':
                        clear()
                        delete_admin()
                    elif con.lower() == 'n':
                        print('Redirect to Main Menu....')
                        clear()
                        admin_menu()
                        break
                else: 
                    delete_admin()
            else:
                input('Not Found This ID Please Try Again ....')
                clear()
                delete_admin()
        except (ValueError,TypeError) as e:
            # print(e)
            print('ID Should Be Number Please Try Again')
            clear()
        except KeyboardInterrupt:
            print('Exit Delete User Mode ...')
            clear()
            admin_menu()
            break

def find_admin():
    while True:
        found_table = PrettyTable()
        try:
            admin_head()
            print('''  _   _   _   _   _   _   _     _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ 
( F | i | n | d | i | n | g ) ( u | s | e | r )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ 
''')
            table_user()
            find_id = input('Find By Name Or ID : ')
            # print(find_id)
            if find_id != '':
                if str(find_id).isnumeric():
                    if check_id(int(find_id)) == int(find_id):
                        ID = int(find_id)
                        name = data[ID]['Name']
                        age = data[ID]['Age']
                        status = data[ID]['Status']
                        balance = data[ID]['money']
                        found_table.field_names = ['ID','Name','Age','Status','Money']
                        print('\nFounding ! ! !')
                        found_table.add_row([ID,name,age,status,balance])
                        print(found_table)
                        con = str(input('\nDo you Want To Find Again ?(y/n)? : '))
                        if con.lower() == 'y':
                            clear()
                            find_admin()
                            break
                        elif con.lower() == 'n':
                            print('Go to Main Admin Menu....')
                            clear()
                            admin_menu()
                            break
                        else: 
                            print('Go to Main Admin Menu....')
                            clear()
                            admin_menu()
                            break
                    else: 
                        input('Not Found Please Try Again...')
                        clear()
                        find_admin()  
                        break
        
                elif str(find_id).isalpha() == False:
                    for id in data.keys():
                        if data[id]['Name'] == str(find_id):
                            name = data[id]['Name']
                            age = data[id]['Age']
                            status = data[id]['Status']
                            balance = data[id]['money']
                            found_table.field_names = ['ID','Name','Age','Status','Money']
                            print('\nFounding ! ! !')
                            found_table.add_row([id,name,age,status,balance])
                            print(found_table)
                            con = str(input('\nDo you Want To Find Again ?(y/n)? : '))
                            if con.lower() == 'y':
                                clear()
                                find_admin()
                            elif con.lower() == 'n':
                                print('Go to Main Admin Menu....')
                                clear()
                                admin_menu()
                                break
                            else: 
                                print('Go to Main Admin Menu....')
                                clear()
                                admin_menu()
                                break
            else:
                input('Your Key Finding Should Not To Blank...')
                clear()
                find_admin()
        except (ValueError,KeyError,TypeError) as e:
            print(e)
        except KeyboardInterrupt :
            print('Exit Finding User Menu...')
            clear()
            admin_menu()
            break



#Function Of User
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
    status = data[id]['Status']
    table_register.field_names = ['Your ID','Name','Status','Balance']
    table_register.add_row([id,name,status,money])
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
            if name.isalpha() :
                surname = str(input('Your Surname is : '))
                if surname.isalpha():
                    if name.isalpha() and surname.isalpha():
                        if name !='' or surname != '':
                            age = int(input("Your Age is : "))
                            if age >= 0 and age<= 20:
                                status = 'STUDYING AGE'
                            elif age >= 21 and age <=59:
                                status = 'WORKING AGE'
                            else:
                                status = 'OLD AGE'
                            fullname = name+' '+surname
                            for id_member in data.keys():
                                if fullname == data[id_member]['Name']:
                                    input('Has this name on our database Please Try Again...') 
                                    clear()
                                    register() 
                            data[id] = {
                                'Name':fullname,
                                'Age':age,
                                'money':0,
                                'Status':status
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
                        clear()
                else: 
                    input('You Surname Should be String not Number Please Try Again...')
                    clear()
                    register()
                    break
            else: 
                input('You Name Should be String not Number Please Try Again...')
                clear()
                register()
                break
        except ValueError: 
            input('Your Age Should Be Number Please Try Again...')
            clear()
        except KeyboardInterrupt:
            print('Exit Register Menu ...')
            clear()
            break
def pay_1():
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
                # Max-(start-stop) ==> 3 to 1
                # ตลอดสาย ==>
                start_b = bus_stop[start]['BName']
                stop_b = bus_stop[stop]['BName']
                user_age = data[user_id]['Age']
                status = data[user_id]['Status']
                if start != 0 and stop !=0:
                    if start > stop:
                        pay=bus_stop[10]['Price']-(bus_stop[start]['Price']-bus_stop[stop]['Price'])
                    elif start == stop:
                        pay=50
                        print('Wrong Destination Please Try Again')
                    else:
                        pay=bus_stop[stop]['Price']-bus_stop[start]['Price']
                print(f'\n=====You are from {start_b} to {stop_b}=====')
                if user_age >=0 and user_age <= 20:
                    rate = 3
                elif user_age >=21 and user_age <= 59:
                    rate = 0
                else:
                    rate = 2
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
                    pay_discount=pay-rate
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
        except KeyboardInterrupt:
            print('Exit Payment Menu ...')
            clear()
            break

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
                
                if topup>=1:
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
                    input('Your Top Up Should be more than 0 Please Try Again...')
                    clear()
                    top_up()
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
                    case '':
                        clear()
                        break
        except (ValueError,TypeError) as e:
            input('Your Money Should Be Only Number Please Try Again...')
            clear()
        except KeyboardInterrupt:
            print('Exit Top Up Menu ...')
            clear()
            break



# Main Programe

while True :
    # edit_admin()
    name_program()
    try:
        print('What Would You Like :\n[0]Exit\n[1]Register\n[2]Pay\n[3]TopUP')
        choose = int(input('Choose : '))
        if choose >= 0 and choose <=3:
            match choose:
                case 0 :
                    break
                case 1 :
                    clear()
                    register()
                case 2 :
                    clear()
                    if pay_1() == 0:
                        break
                case 3 :
                    clear()
                    top_up()
        elif choose == 1001:
            clear()
            login_admin()
        else:
            input('0 1 2 3 Only Please Try Again...')
            clear()
    except (ValueError,TypeError):
        input('Only Number Please Try Again...')
        clear()
