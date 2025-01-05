#Library and Value
from random import * 

data = {25032:{'Name':'Naphop Khumchawna','Age':25,'money':50},24354:{'Name':'Veeraya Lekchaaum','Age':17,'money':40},74512:{'Name':'Klittima Chawwadee','Age':19,'money':50}}
bus_stop = {1:{'BName':'Busta Shinjuku','Price':5},2:{'BName':'Tomigaya','Price':10},3:{'BName':'Sakurabashi','Price':15},4:{'BName':'Namsan Seoul Tower','Price':20},5:{'BName':'Seoul Arts Center','Price':25},6:{'BName':'Myeong-dong Entrance','Price':30},7:{'BName':'Seoul Square','Price':35},8:{'BName':'Bridge St','Price':40},9:{'BName':'Manchester Coach Station','Price':45},10:{'BName':'Manchester Shudehill','Price':50}}


#Function
def show_id(id):
    name = data[id]['Name']
    money = data[id]['money']
    return print(f'\nYour ID is {id}\nWelcome {name}\nYour Balance is {money}')
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
    return num

def register():
    while True:
        try:
            id = gen_id()
            name = str(input("Your Name is : "))
            surname = str(input('Your Surname is : '))
            age = int(input("Your Age is : "))    
            fullname = name+' '+surname
            for id_member in data.keys():
                if fullname == data[id_member]['Name']:
                    print('Has IT') 
                    register() 
            data[id] = {
                'Name':fullname,
                'Age':age,
                'money':0
                }
            show_id(id)
            clear()
            break
        except ValueError: 
            print('Your Age Should Be Number Please Try Again')
def pay():
    while True:
        try: 
            user_id=int(input("Your ID :"))
            if check_id(user_id) == user_id:
                print(f'HI {data[user_id]["Name"]} Your balance is : {data[user_id]["money"]}\n')
                # print(data)
                money=data[user_id]['money']
                print('Bus Stop List')
                for select in bus_stop.keys():
                    print(select,bus_stop[select]['BName'])
   
                start=int(input("Choose Start Station : "))
                stop=int(input("Choose Stop Station : "))
                start_b = bus_stop[start]['BName']
                stop_b = bus_stop[stop]['BName']
                user_age = data[user_id]['Age']
                pay=bus_stop[stop]['Price']-bus_stop[start]['Price']
                print(f'\nYou are from {start_b} to {stop_b}')
                if user_age >=0 and user_age <= 20:
                    rate = 3
                elif user_age >=21 and user_age <= 59:
                    rate = 0
                else:
                    rate = 2
                if pay>data[user_id]['money']:
                    print('Your balance is not sufficient')
                    choose = str(input('Would You Like To Top Up ? (y/n) : '))
                    if choose.lower() == 'y':
                        clear()
                        top_up()
                        break
                    elif choose.lower() == 'n':
                        break 
                    else:
                        print('Please Try Again...')
                        clear()
                        break                       
                else:
                    pay_discount=bus_stop[stop]['Price']-bus_stop[start]['Price']-rate
                    stable = data[user_id]['money']-pay_discount
                    data[user_id]['money'] = stable
                    print(f'\nYou Have Got in Your Account For {money} \nFull Price is {pay}\nYou are {user_age} years old\nYou Have Got The Discount for {rate}\nSo you should pay for {pay_discount}\nYour Balance is {stable}')
                    farewell(data[user_id]['Name'])
                    return 0
            else:
                print('Not Found Your ID Please Try Again')
                choose = str(input('Do You Want to Go To Main Menu ? (y/n) : '))
                if choose.lower() == 'y':
                    break
                elif choose.lower()=='n':
                    pass
        except (TypeError,ValueError) : 
            print('It Should Be Number')
def top_up():
    while True:
        try:
            user_id=int(input("Your ID : "))
            if check_id(user_id) == user_id:
                money=data[user_id]['money']
                name=data[user_id]['Name']
                print(f'\nHi {name} Your Balance is {money}')
                topup=int(input('Topup : '))
                money += topup
                data[user_id]['money'] = money
                print('\nSuccessfully ! ! ! ! ')
                print(f'Account : {name} Has Balance is {money}')
                print('Thank You For Top Up')
                break
            else:
                print('Not Found This ID')
        except (ValueError,TypeError):
            print('Your Money Should Be Only Number')


# Main Programe
while True :
    try:
       
        print('\n[0]Exit\n[1]Register\n[2]Pay\n[3]TopUP')
        choose = int(input('Choose : '))
        match choose:
            case 0 :
                break
            case 1 :
                register()
            case 2 :
                if pay() == 0:
                    break
            case 3 :
                top_up()
    except (ValueError,TypeError):
        print('Only Number Please Try Again')
